class Solution:
    def completePrime(self, num: int) -> bool:
        s = str(num)

        # Check all prefixes
        for i in range(1, len(s) + 1):
            prefix = int(s[:i])
            if not self.isPrime(prefix):
                return False

        # Check all suffixes
        for i in range(len(s)):
            suffix = int(s[i:])
            if not self.isPrime(suffix):
                return False

        return True

    def isPrime(self, n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True