Launch with default parameters :
./run.sh

Launch with custom parameters :
./run.sh [csv_subdir] [generations_amount] [time_limit_in_seconds]
Or :
./run.sh [csv_subdir] [generations_amount] [time_limit_in_seconds] [population_size]

If the time limit is 0 or less, there is no time limit.
If the time limit is greater than 0 the amount of generations is ignored and the program will stop when the time is over.