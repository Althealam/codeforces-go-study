class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        diff = [0]*n
        # get the difference array
        for booking in bookings:
            first, last = booking[0], booking[1]
            reserved_seats = booking[2]
            diff[first-1]+=reserved_seats
            if last<n:
                diff[last]-=reserved_seats
        
        array = [0]*n
        array[0] = diff[0]
        for i in range(1, len(array)):
            array[i]=array[i-1]+diff[i]
        return array

bookings = [[1,2,10],[2,3,20],[2,5,25]]
n=3
sol = Solution()
res = sol.corpFlightBookings(bookings, n)
print(res)