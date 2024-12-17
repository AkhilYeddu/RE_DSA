months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
current = input()
k = int(input())
current_i = months.index(current)
new = (current_i+k) % 12
print(months[new])