# Data Partitioning

**A technique for breaking large data sets into smaller, more manageable pieces called partitions, each of which is distributed across different nodes or servers.**

## Why we should use that?

### Scalability
Allows for the storage and processing of data much larger than the capacity of a single machine.

### Performance Improvement
Queries are executed only on a specific partition instead of scanning the entire table, which increases speed.

### Load Balancing
Read/write load is divided across multiple nodes, preventing bottlenecks.

### Better Management
Each partition can be maintained, backed up, and optimized independently of the others.

### Fault Tolerance
If one partition or node fails, the rest of the system continues to function.

## Type of DP

### Horizontal Partitioning
Partition data by rows; each partition contains a subset of records.
- Users with different IDs on different servers.

### Vertical Partitioning
Partition data by columns; each partition contains a subset of fields.
- Separating heavily used columns from bulky or underused columns.

### Range Partitioning
Data is partitioned based on a range of values ​​for a key.
- Data for 2024 in one partition, 2025 in another.

### List Partitioning
Data is partitioned based on a list of specified values.
- Iranian users in one partition, European users in another.

### Directory-Based Partitioning
A lookup service maintains a key-to-partition mapping.
- Systems that require high flexibility in moving data.

### Hash Partitioning
The destination partition is determined by applying a hash function to the key.
- Evenly distribute data and reduce hotspots.

### Functional Partitioning
Partitioning based on type of function or workload (e.g., separating transactional databases from reporting databases).
- Microservice systems with separate responsibilities.
