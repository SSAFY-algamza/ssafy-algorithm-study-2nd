/*
 * dfs - 진행 방향으로 계속 진행 후 끝에 도착하면 돌아와 다시 시작
 * minHeap - 부모가 자식보다 항상 작음을 보장하는 완전 이진 트리
 * 
 * 문제와 예제를 보면 싸이클을 이루게 된다면 답이 된다.
 * 
 * 힙(Heap) 클래스와 입력을 받기 위한 함수(read())를 구현했다.
 * 입력 받은 배열들을 dfs로 방문 체크를 하며 탐색한다.
 * 탐색을 하다 이미 방문한 곳을 만난다면 싸이클이 형성됨으로 그 지점을 힙에 담아준다.
 * 
 * 시간 복잡도 - heap을 사용해 입력받을 때마다 정렬로 NlogN이지만, dfs엔 N^2임으로 "O(n^2)"
 * 공간 복잡도 - heap 배열에 N + 1, 입력 받은 배열에 N + 1임으로 "O(N)"
 */

class P2668 {

    static class Heap {
        int[] heap;
        int size;

        Heap(int size) {
            this.heap = new int[size + 1];
        }

        void offer(int x) {
            heap[++size] = x;
            int i = size << 1;

            while ((i >>= 1) > 1) {
                if (!swap(i)) {
                    break;
                }
            }
        }

        int poll() {
            int x = heap[1];
            heap[1] = heap[size--];
            int i = 1;

            while ((i <<= 1) <= size) {
                if (i < size && heap[i + 1] < heap[i]) {
                    i++;
                }

                if (!swap(i)) {
                    break;
                }
            }

            return x;
        }

        boolean swap(int i) {
            int j = i >> 1;
            int parent = heap[j];
            int child = heap[i];

            if (parent < child) {
                return false;
            }

            heap[j] = child;
            heap[i] = parent;

            return true;
        }
    }

    static Heap heap;
    static boolean[] visited;
    static int[] arr;

    public static void main(String[] args) throws Exception {
        StringBuilder sb = new StringBuilder();
        int N = read();

        heap = new Heap(N);
        visited = new boolean[N + 1];
        arr = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            arr[i] = read();
        }

        for (int i = 1; i <= N; i++) {
            visited[i] = true;
            dfs(i, i);
            visited[i] = false;
        }

        sb.append(heap.size).append('\n');

        while (heap.size > 0) {
            sb.append(heap.poll()).append('\n');
        }

        System.out.print(sb);
    }

    static void dfs(int start, int target) {
        if (visited[arr[start]] == false) {
            visited[arr[start]] = true;
            dfs(arr[start], target);
            visited[arr[start]] = false;
        }

        if (arr[start] == target) {
            heap.offer(target);
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
