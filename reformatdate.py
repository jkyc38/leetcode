class Solution:
    def reformatDate(self, date: str) -> str:
        map = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}

        split = date.split(sep=" ")
        

        formatted = ""

        formatted+=f"{split[2]}-"

        formatted+=f'{map[split[1]]}-'
        print(date[0])
        
        if len(split[0])<4:
            formatted+="0"
        for c in split[0]:
            
            #get day lol
            print(c)
            if c.isalpha():
                continue
            else:
                formatted+=c
        return formatted
    def reformatDate2(self, date: str):
        map = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}

        split = date.split(sep=" ")
        #split[0] day
        #split[1] month
        #split[2] year

        year = split[2]
        month = map[split[1]]
        day = split[0][:-2]
        if int(day)<10:
            day = f'0{day}'
        
        return f'{year}-{month}-{day}'
        

date = "6th Jun 1933"

sol = Solution()

n = sol.reformatDate2(date)
print(n)