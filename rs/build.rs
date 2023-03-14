// for compiling proto files

fn main() -> Result<(), Box<dyn std::error::Error>> {
    tonic_build::compile_protos("proto/dataquery.proto")?;
    Ok(())
}