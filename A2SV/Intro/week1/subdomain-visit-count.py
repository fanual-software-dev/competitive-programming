class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        ans = []

        ans_dict = {}

        for domains in cpdomains:

            value, other = domains.split()

            ans = other.split(".")


            for i in range(len(ans)):

                ans_dict [".".join(ans[i:])]= int(value) + ans_dict.get(".".join(ans[i:]),0)

        rans = [f'{value} {key}' for key ,value in ans_dict.items()]

        return rans 
        