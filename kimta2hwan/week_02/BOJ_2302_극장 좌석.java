/*
 * dp - 하나의 큰 문제를 작은 문제로 나누어 해결하는 기법
 * 
 * VIP으로 구간을 쪼개어 구간 마다 dp를 구한 후 각각 곱해준다.
 * 
 * N이 1 또는 2이면 예외 처리를 해줘야 하기 때문에 dp 배열을 41로 고정으로 생성해준다.
 * 또한 VIP가 1과 같은 경우 dp[0]가 0이면 결과가 0이기 때문에 dp[0]를 1로 만들어준다.
 * dp식을 이용해 40까지의 dp를 모두 구한다.
 * 그 후 각 구간마다의 dp를 구하고 곱해준다.
 * 
 * 시간 복잡도 - O(N)
 * 공간 복잡도 - O(N)
 */

class P2302 {
    public static void main(String[] args) throws Exception {
        int N = read();
        int M = read();

        int[] dp = new int[41];

        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;

        for (int i = 3; i <= N; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        int answer = 1;
        int before = 0;

        while (M-- > 0) {
            int vip = read();
            answer *= dp[vip - before - 1];
            before = vip;
        }

        answer *= dp[N - before];
        System.out.print(answer);
    }

    private static int read() throws Exception {
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
