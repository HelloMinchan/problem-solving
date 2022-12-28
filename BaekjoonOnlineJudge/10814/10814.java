import java.io.*;
import java.util.*;
import java.util.stream.*;

class Tuple {

    int age;
    int sequence;
    String name;


    Tuple(int age, int sequence, String name) {
        this.age = age;
        this.sequence = sequence;
        this.name = name;
    }
}

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int userCount = Integer.parseInt(br.readLine());

        ArrayList<Tuple> users = new ArrayList<>();

        for (int sequence = 0; sequence < userCount; sequence++) {
            st = new StringTokenizer(br.readLine());

            int age = Integer.parseInt(st.nextToken());
            String name = st.nextToken();

            users.add(new Tuple(age, sequence, name));
        }

        Collections.sort(users, (user1, user2) -> {
            if (user1.age > user2.age) {
                return 1;
            } else if (user1.age < user2.age) {
                return -1;
            } else {
                if (user1.sequence > user2.sequence) {
                    return 1;
                } else {
                    return -1;
                }
            }
        });

        for (Tuple user : users) {
            bw.write(user.age + " " + user.name + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}