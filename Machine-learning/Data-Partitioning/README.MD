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