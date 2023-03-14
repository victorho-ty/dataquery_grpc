use dataquery::data_query_client::DataQueryClient;
use dataquery::GetDataRequest;
use dataquery::MetadataRequest;

// new module to include types based on proto file
pub mod dataquery {
    tonic::include_proto!("dataquery");
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut client = DataQueryClient::connect("http://[::1]:9999").await?;

    // #1 RPC call to get_data()  
    let data_req = tonic::Request::new(
        GetDataRequest {
            user_id: "victor.ty.ho".to_owned(),
            user_token: "wqeadsAATYGDGDqwwqeadsAATYGDGDqw".to_owned(),
            data_id:  "ZN".to_owned(),
            data_type: "snap.NKY".to_owned(),
            return_type: 0,  
        }
    );
    let response = client.get_data(data_req).await?;
    println!("get_data RESPONSE={:?}", response);

    // #2 RPC call to inspect_metadata()
    let meta_req = tonic::Request::new(
        MetadataRequest {
            user_id: "victor.ty.ho".to_owned(),
            user_token: "wqeadsAATYGDGDqwwqeadsAATYGDGDqw".to_owned(),
            data_id:  "JGB10Y".to_owned(),
            data_type: "snap.TSE".to_owned(),
        }
    );

    let response2 = client.inspect_metadata(meta_req).await?;
    println!("inspect_metadata RESPONSE={:?}", response2);

    Ok(())
}