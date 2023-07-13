import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

/*
 * BFS - 한 정점에서 갈 수 있는 곳을 동시에 가면서 탐색한다.
 * 
 * 시간 복잡도 O(N * M), 공간 복잡도 O(2 * N ^ 2)
 */

class P15591 {

    private static List<int[]>[] list;
    private static int N, Q;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());

        list = new ArrayList[N + 1];

        for (int i = 1; i <= N; i++) {
            list[i] = new ArrayList<>();
        }

        for (int i = 1; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int p = Integer.parseInt(st.nextToken());
            int q = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());

            list[p].add(new int[]{q, r});
            list[q].add(new int[]{p, r});
        }

        while (Q-- > 0) {
            st = new StringTokenizer(br.readLine());

            boolean[] visited = new boolean[N + 1];
            int k = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int answer = 0;

            Queue<Integer> queue = new ArrayDeque<>();
            visited[v] = true;
            queue.offer(v);
            
            while (!queue.isEmpty()) {
                int curr = queue.poll();

                for (int[] arr : list[curr]) {
                    if (!visited[arr[0]] && arr[1] >= k) {
                        visited[arr[0]] = true;
                        queue.offer(arr[0]);
                        answer++;
                    }
                }
            }

            sb.append(answer).append('\n');
        }

        System.out.print(sb);
    }
}
