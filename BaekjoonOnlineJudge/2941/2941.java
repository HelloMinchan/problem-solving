import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        char[] word = br.readLine().toCharArray();
        int answer = 0;

        for (int index = 0; index < word.length; index++) {
            answer++;

            if (word[index] == 'd') {
                if (index + 1 < word.length) {
                    index++;
                } else {
                    break;
                }

                if (word[index] == '-') {
                    if (index + 1 >= word.length) {
                        break;
                    }
                } else {
                    if (word[index] == 'z') {
                        if (index + 1 < word.length) {
                            index++;
                        } else {
                            index--;
                            continue;
                        }

                        if (word[index] == '=') {
                            if (index + 1 >= word.length) {
                                break;
                            }
                        } else {
                            index -= 2;
                        }
                    } else {
                        index--;
                    }
                }
            } else if (word[index] == 'l' || word[index] == 'n') {
                if (index + 1 < word.length) {
                    index++;
                } else {
                    break;
                }

                if (word[index] == 'j') {
                    if (index + 1 >= word.length) {
                        break;
                    }
                } else {
                    index--;
                }
            } else if (word[index] == 's' || word[index] == 'z') {
                if (index + 1 < word.length) {
                    index++;
                } else {
                    break;
                }

                if (word[index] == '=') {
                    if (index + 1 >= word.length) {
                        break;
                    }
                } else {
                    index--;
                }
            } else if (word[index] == 'c') {
                if (index + 1 < word.length) {
                    index++;
                } else {
                    break;
                }

                if (word[index] == '=' || word[index] == '-') {
                    if (index + 1 >= word.length) {
                        break;
                    }
                } else {
                    index--;
                }
            }
        }

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}