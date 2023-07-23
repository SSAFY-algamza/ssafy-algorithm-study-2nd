/*
 * 백트래킹 - 완전탐색을 진행하긴 하지만 중간에 조건을 두어 조건을 만족하면 종료하는 기법
 * 
 * 각 빈 곳마다 벽을 한번씩 세우고 3개를 세울때마다 선생님의 시야를 확인 해준다.
 * 
 * 입력 받은 지도를 한 점씩 빈곳을 기둥으로 바꾸고 다시 재귀함수를 돌려준다.
 * 재귀가 종료되면 기둥으로 바꾼곳을 다시 빈곳으로 바꾸어준다.
 * 기둥의 개수가 3개가 된다면 각 선생님의 시야를 확인해준다.
 * 선생님의 시야에 학생이 들어온다면 해당 재귀를 종료해준다.
 * 선생님의 시야에 기둥이 들어온다면 시야 확인을 종료해주고 계속 진행 해 준다.
 * 
 * 시간 복잡도 - O(N^2)
 * 공간 복잡도 - O(N^2)
 */

import java.util.ArrayList;
import java.util.List;

class P18428 {

    static class Teacher {
        int r;
        int c;

        Teacher(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    static List<Teacher> teachers;
    static boolean[][] visited;
    static int[][] map;
    static boolean flag;
    static int N;

    public static void main(String[] args) throws Exception {
        N = read();

        teachers = new ArrayList<>();
        visited = new boolean[N][N];
        map = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                map[i][j] = read();

                if (map[i][j] == 4) {
                    teachers.add(new Teacher(i, j));
                }
            }
        }

        backTracking(0, 0);
        System.out.print(flag ? "YES" : "NO");
    }

    static void backTracking(int count, int index) {
        if (flag) {
            return;
        }

        if (count == 3) {
            for (Teacher teacher : teachers) {
                for (int i = 0; i < 4; i++) {
                    int nr = teacher.r + dr[i];
                    int nc = teacher.c + dc[i];

                    while (nr >= 0 && nr < N && nc >= 0 && nc < N) {
                        if (map[nr][nc] == 3) {
                            return;
                        }

                        if (map[nr][nc] == 15) {
                            break;
                        }

                        nr += dr[i];
                        nc += dc[i];
                    }
                }
            }

            flag = true;
            return;
        }

        for (int i = index; i < N * N; i++) {
            if (map[i / N][i % N] == 8) {
                map[i / N][i % N] = 15;
                backTracking(count + 1, i + 1);
                map[i / N][i % N] = 8;
            }
        }
    }

    static int read() throws Exception {
        int c, n = System.in.read() & 15;

        while ((c = System.in.read()) > 32) {
            n = (n << 3) + (n << 1) + (c & 15);
        }

        if (c == 13) {
            System.in.read();
        }

        return n;
    }
}
