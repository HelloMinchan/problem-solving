import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        int neverHeardPeopleCount = Integer.parseInt(st.nextToken());
        int neverSeenPeopleCount = Integer.parseInt(st.nextToken());

        Map<String, Integer> nameCountDict = new HashMap<>();

        while (neverHeardPeopleCount-- != 0) {
            String name = br.readLine();
            nameCountDict.put(name, 1);
        }

        while (neverSeenPeopleCount-- != 0) {
            String name = br.readLine();

            if (nameCountDict.containsKey(name)) {
                nameCountDict.put(name, nameCountDict.get(name) + 1);
            } else {
                nameCountDict.put(name, 1);
            }
        }

        ArrayList<String> neverHeardNeverSeenPeople = new ArrayList<>();

        nameCountDict.entrySet().forEach((entry) -> {
            if (entry.getValue() == 2) {
                neverHeardNeverSeenPeople.add(entry.getKey());
            }
        });

        System.out.println(neverHeardNeverSeenPeople.size());
        neverHeardNeverSeenPeople.stream().sorted().forEach(System.out::println);

        bw.flush();
        bw.close();
        br.close();
    }
}