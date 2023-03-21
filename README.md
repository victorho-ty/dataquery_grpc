## Data Query
Prototype for GPRC across Rust, Python for data query purpose.


### Rust
#### Server (Run)
cargo run --bin dataquery-server

#### Client (Run)
cargo run --bin dataquery-client

#### Tests
cargo test <module_name>
cargo test <test_fn_name_substring>

### Python 
#### protoc command
python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/dataquery.proto

#### Client (Run)
python py/dataquery_client.py
