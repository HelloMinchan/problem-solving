import java.io.*;
import java.util.*;

class Coordinate {

    int x;
    int y;

    Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return this.x;
    }

    public int getY() {
        return this.y;
    }
}

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        ArrayList<Coordinate> coordinates = new ArrayList<>();

        while (n-- != 0) {
            st = new StringTokenizer(br.readLine());

            coordinates.add(
                new Coordinate(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }

        coordinates.stream()
            .sorted(Comparator.comparing(Coordinate::getY).thenComparing(Coordinate::getX))
            .forEach(coordinate -> System.out.println(coordinate.getX() + " " + coordinate.getY()));

        bw.flush();
        bw.close();
        br.close();
    }
}