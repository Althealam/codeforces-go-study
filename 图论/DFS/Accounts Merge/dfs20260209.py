from collections import defaultdict
# 建立邻接表，连接各个email：email_to_email = {email: set(connected_emails)}
# 建立邻接表，连接各个email和人：email_to_name = {email: name}
class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        email_to_email = defaultdict(set) # 建立从email到email的graph
        email_to_name = defaultdict() # 建立从email到名字的graph
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                email_to_email[first_email].add(email)
                email_to_email[email].add(first_email)
                email_to_name[email] = name

        def dfs(email, component):
            component.append(email) # 一定要写在前面，否则会将起点节点忽略
            if email not in visited:
                visited.add(email)
            for neighbor_email in email_to_email[email]:
                if neighbor_email not in visited:
                    dfs(neighbor_email, component)
       
        visited = set()
        res = []
        for email in email_to_email: # iterate all email
            if email not in visited:
                component = [] # 获取该email所关联的所有其他emails
                dfs(email, component) # dfs遍历该email所有的邻居节点
                res.append([email_to_name[email]]+sorted(component))

        return res

             

accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
solution = Solution()
res = solution.accountsMerge(accounts)
print(res)