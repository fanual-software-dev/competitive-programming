class AuthenticationManager:

    def __init__(self, timeToLive: int):
        
        self.timeTolive = timeToLive

        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        
        self.tokens[ tokenId ] = currentTime + self.timeTolive

    def renew(self, tokenId: str, currentTime: int) -> None:

        if tokenId in self.tokens and  self.tokens[tokenId]>currentTime:
        
            self.tokens[tokenId] = currentTime +self.timeTolive

    def countUnexpiredTokens(self, currentTime: int) -> int:

        unexpired = 0

        for i in self.tokens.values():

           if i>currentTime: unexpired +=1

        return unexpired

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)