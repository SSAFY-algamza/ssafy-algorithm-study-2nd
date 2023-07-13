import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * dp는 하나의 큰 문제를 여러개의 작은 문제로 나누어서 그 결과를 저장하여 다시 큰 문제를 해결할 때 사용하는 것으로 특정한 알고리즘이 아닌 하나의 문제해결 패러다임
 * 
 * 그림으로 밖에 설명을 못 하겠어요....
 * 
 * 전형적인 dp 코드이다.
 * 
 * 시간 복잡도 O(N), 공간 복잡도 O(40004)?
 */

class P15989 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int[][] dp = new int[10001][4];
        int T = Integer.parseInt(br.readLine());

        dp[1][1] = 1;
        dp[2][1] = 1;
        dp[2][2] = 1;
        dp[3][1] = 1;
        dp[3][2] = 1;
        dp[3][3] = 1;

        for (int i = 4; i <= 10000; i++) {
            dp[i][1] = dp[i - 1][1];
            dp[i][2] = dp[i - 2][1] + dp[i - 2][2];
            dp[i][3] = dp[i - 3][1] + dp[i - 3][2] + dp[i - 3][3];
        }

        while (T-- > 0) {
            int n = Integer.parseInt(br.readLine());
            sb.append(dp[n][1] + dp[n][2] + dp[n][3]).append('\n');
        }

        System.out.print(sb);
    }
}
