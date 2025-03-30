# Q7. EC2 Recommendation
# Python script that provides EC2 instance recommendations based on a given instance's type, size, and CPU utilization. The script will help in recommending appropriate EC2 instances for optimizing performance and costs based on the utilization metrics.
# Input:
# Current EC2 Instance: A string representing the instance type and size (e.g., t2.nano, t3.medium).
# CPU Utilization: A percentage value representing the current CPU utilization (e.g., 40%).

# The output will be a recommendation for a new EC2 instance based on the following logic:

# Underutilized: If the CPU utilization is less than 20%, recommend a smaller instance.
# Optimized: If the CPU utilization is between 20% and 80%, recommend the same instance size but suggest the latest generation instance type.
# Overutilized: If the CPU utilization is greater than 80%, recommend a larger instance.
 
# Instance Size Comparison: The EC2 instance sizes follow a specific hierarchy:

# nano > micro > small > medium > large > xlarge > 2xlarge > 4xlarge > 8xlarge > 16xlarge > 32xlarge..

# If the CPU is underutilized (CPU < 20%), the script should recommend a smaller instance by one step.
# If the CPU is overutilized (CPU > 80%), the script should recommend a larger instance by one step.
# If the instance size is the smallest (nano), it cannot be reduced further, so no smaller size is recommended.
# If the instance is the largest (32xlarge), it cannot be upgraded further.

# Input 1: 
# Current EC2 : t2.large
# CPU : 20%

# Output 1:
# Table showing columns and its value (use Que 6 function to make table with following columns)
# Columns are : serial no., current ec2, current CPU, status, recommended ec2


import re

def get_instance_family(instance_type):
    """Extracts instance family and size from instance type."""
    match = re.match(r"([a-z]+[0-9]+)\.(nano|micro|small|medium|large|xlarge|\d+xlarge)", instance_type)
    return match.groups() if match else (None, None)

def get_recommendation(instance_type, cpu_utilization):
    """Provides EC2 instance recommendations based on CPU utilization."""
    instance_family, instance_size = get_instance_family(instance_type)
    
    if not instance_family or not instance_size:
        return "Invalid instance type"
    
    sizes = ["nano", "micro", "small", "medium", "large", "xlarge", "2xlarge", "4xlarge", "8xlarge", "16xlarge", "32xlarge"]
    size_index = sizes.index(instance_size)
    
    if cpu_utilization < 20 and size_index > 0:
        recommended_size = sizes[size_index - 1]
        status = "Underutilized"
    elif cpu_utilization > 80 and size_index < len(sizes) - 1:
        recommended_size = sizes[size_index + 1]
        status = "Overutilized"
    else:
        recommended_size = instance_size
        status = "Optimized"
    
    recommended_instance = f"{instance_family}.{recommended_size}"
    return [(1, instance_type, f"{cpu_utilization}%", status, recommended_instance)]

def print_table(data):
    """Prints data in a formatted table."""
    headers = ["Serial No.", "Current EC2", "Current CPU", "Status", "Recommended EC2"]
    col_widths = [max(len(str(row[i])) for row in data + [headers]) for i in range(len(headers))]
    
    print(" | ".join(header.ljust(col_widths[i]) for i, header in enumerate(headers)))
    print("-" * (sum(col_widths) + len(headers) * 3 - 1))
    
    for row in data:
        print(" | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(headers))))

if __name__ == "__main__":
    current_ec2 = "t2.large"
    cpu_utilization = 20
    
    recommendation = get_recommendation(current_ec2, cpu_utilization)
    print_table(recommendation)
