class Codec:
    hash_key = 0
    encode_hash = dict()
    decode_hash = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        encoded_url = ""

        for partition in longUrl.split("/"):
            if Codec.encode_hash.get(partition, False):
                encoded_url += Codec.encode_hash.get(partition, False) + "/"
            else:
                if partition == "":
                    encoded_url += "/"
                else:
                    Codec.encode_hash[partition] = str(Codec.hash_key)
                    Codec.decode_hash[Codec.hash_key] = partition

                    encoded_url += str(Codec.hash_key) + "/"
                    Codec.hash_key += 1
        
        return encoded_url[:-1]
        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        decoded_url = ""

        for partition in shortUrl.split("/"):
            if partition == "":
                decoded_url += "/"
            else:
                decoded_url += Codec.decode_hash[int(partition)] + "/"
        
        return decoded_url[:-1]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))