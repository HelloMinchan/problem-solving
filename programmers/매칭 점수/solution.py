from collections import defaultdict


def parse_meta_url(page):
    meta_url = page.split('<meta property="og:url" content="')[1]

    return meta_url.split('"/>')[0]


def parse_out_link(in_links, out_links, url, body_string):
    out_link_candidates = body_string.split('<a href="')

    for out_link_candidate in out_link_candidates:
        if "https://" in out_link_candidate:
            out_link = out_link_candidate.split('">')[0]
            out_links[url].append(out_link)
            in_links[out_link].append(url)


def solution(word, pages):
    word = word.lower()
    urls = []
    basic_scores = defaultdict(int)
    in_links = defaultdict(list)
    out_links = defaultdict(list)

    for page in pages:
        # parse head
        url = parse_meta_url(page)
        urls.append(url)

        # parse body
        body = page.split("<body>")[1]
        body_strings = body.split("</body>")[0].split("\n")

        basic_score = 0
        for body_string in body_strings[1 : len(body_strings) - 1]:
            body_string = body_string.lower()

            body_string_start_index = body_string_index = 0

            while body_string_index < len(body_string):
                if not body_string[body_string_index].isalpha():
                    if body_string[body_string_start_index:body_string_index] == word:
                        basic_score += 1

                    body_string_start_index = body_string_index + 1
                body_string_index += 1

            if body_string_start_index != len(body_string):
                if body_string[body_string_start_index:body_string_index] == word:
                    basic_score += 1

            parse_out_link(in_links, out_links, url, body_string)

        basic_scores[url] = basic_score

    answer = []
    for index, url in enumerate(urls):
        basic_score = basic_scores[url]

        link_score = 0

        for in_link in in_links[url]:
            link_score += basic_scores[in_link] / len(out_links[in_link])

        answer.append((basic_score + link_score, index))

    answer.sort(key=lambda answer: (-answer[0], answer[1]))

    return answer[0][1]
