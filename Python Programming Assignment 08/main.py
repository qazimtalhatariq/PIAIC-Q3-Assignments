print("Welcome to the Water Jug Puzzle!")
print("The goal is to fill one of the buckets with 4L of water.\n\n")

print("8|      |")
print("7|      |")
print("6|      |")
print("5|      |   5|      |")
print("4|      |   4|      |")
print("3|      |   3|      |   3|      |")
print("2|      |   2|      |   2|      |")
print("1|      |   1|      |   1|      |")

print(" +------+    +------+    +------+")
print("    8L          5L          3L")

def main():
       buckets = [0, 0, 0]  # Initialize with 0 to fix the error
       while True:
           print("Try to get 4L of water into one of these buckets:\n")
           print_buckets(buckets)
           print("\nYou can:")
           print("(F)ill the bucket")
           print("(E)mpty the bucket")
           print("(P)our one bucket into another")
           print("(Q)uit")
           action = input("> ").upper()

           if action == "F":
               bucket_num = get_bucket_number()
               fill_bucket(buckets, bucket_num)
               print_buckets(buckets)
           elif action == "E":
               bucket_num = get_bucket_number()
               empty_bucket(buckets, bucket_num)
               print_buckets(buckets)
           elif action == "P":
               source_bucket = get_bucket_number()
               target_bucket = get_bucket_number()
               pour_water(buckets, source_bucket, target_bucket)
               print_buckets(buckets)
           elif action == "Q":
               print("Quitting...")
               break
           else:
               print("Invalid action. Please try again.")

           if any(bucket == 4 for bucket in buckets): # Fix the win condition
               print("Congratulations! You have 4L of water in one of the buckets.")
               break

def get_bucket_number():
        while True:
            try:
                bucket_num = int(input("Select a bucket 8, 5, 3, or QUIT: "))
                if bucket_num in [8, 5, 3]:
                    return bucket_num
                else:
                    print("Invalid bucket number. Please enter 8, 5, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

def fill_bucket(buckets, bucket_num):
       buckets[bucket_num - 1] = bucket_num  # Assign bucket's capacity

def empty_bucket(buckets, bucket_num):
    buckets[bucket_num - 1] = 0

def pour_water(buckets, source_bucket, target_bucket):
       source_water = buckets[source_bucket - 1]
       target_water = buckets[target_bucket - 1]
       remaining_space = target_bucket - target_water  # Fix capacity calculation
       if source_water <= remaining_space:
           buckets[target_bucket - 1] += source_water
           buckets[source_bucket - 1] = 0
       else:
           buckets[target_bucket - 1] = target_bucket  # Fill target bucket
           buckets[source_bucket - 1] -= remaining_space  # Update source bucket

def print_buckets(buckets):
    for i in range(8, 0, -1):
        line = ""
        for bucket_capacity, water_level in zip([8, 5, 3], buckets):  # Get capacity and water level
            if water_level >= i:
                line += "   W"  # Print 'W' if water level is at or above current line
            else:
                line += "    "  # Print empty space otherwise
            line += "   "  # Add space between buckets
        print(line)  # Print the line for the current water level
    print("  +------+   +------+   +------+")
    print(f"     {buckets[0]}L          {buckets[1]}L          {buckets[2]}L          ")  # Print water levels

if __name__ == "__main__":
    main()
