earth_days, earth_hours = map(int, input("Please enter Earth day and Earth hours divided by , and space: ").split(", "))
sol: float = round((earth_days + earth_hours / 24) * 1.02595675, 2)
result_message: str = f"The number of Earth days entered will be equal to {sol} sols on Mars"
print(result_message)
