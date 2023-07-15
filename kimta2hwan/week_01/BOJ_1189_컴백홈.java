import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
 * DFS - 계속 진행 방향으로 진행하다가 더 이상 진행할 수 없으면 뒤로 돌아와 다시 탐색한다.
 * 
 * 그래프 탐색이다.
 * 최단 거리가 아닌 진행한 상황이 계속해서 이어져야 하기 때문에 bfs가 아닌 dfs로 접근했다.
 * 
 * 1. 입력을 받는다.
 * 2. dfs를 실행한다.
 * 3. 사방 탐색을 실행해준다.
 * 4. 주의사항으로는 깊이 우선 탐색이기 때문에 들어가기 전엔 방문처리를 해주고 후엔 방문처리를 취소 해준다.
 * 
 * 시간 복잡도 O(R * C)?, 공간 복잡도 O(R * C)
 */

class P1189 {

    private static int[] dr = {-1, 0, 0, 1};
    private static int[] dc = {0, 1, -1, 0};

    private static boolean[][] visited;
    private static char[][] map;
    private static int R, C, K, answer;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        visited = new boolean[R][C];
        map = new char[R][C];

        for (int i = 0; i < R; i++) {
            map[i] = br.readLine().toCharArray();
        }

        visited[R - 1][0] = true;
        dfs(R - 1, 0, 1);

        System.out.print(answer);
    }

    private static void dfs(int r, int c, int count) {
        if (r == 0 && c == C - 1 && count == K) {
            answer++;
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (nr < 0 || nr >= R || nc < 0 || nc >= C || visited[nr][nc] || map[nr][nc] == 'T') {
                continue;
            }

            visited[nr][nc] = true;
            dfs(nr, nc, count + 1);
            visited[nr][nc] = false;
        }
    }
}
