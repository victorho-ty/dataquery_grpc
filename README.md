## Data Query
Prototype for GPRC across Rust, Python for data query purpose.


### Rust
#### Server (Run)
cargo run --bin dataquery-server

#### Client (Run)
cargo run --bin dataquery-client


### Python 
#### protoc command
python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/dataquery.proto

#### Client (Run)
python py/dataquery_client.py
