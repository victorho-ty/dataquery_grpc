use dataquery::data_query_client::DataQueryClient;
use dataquery::GetDataRequest;
use dataquery::MetadataRequest;
//#[cfg(test)]
//use mockall::{automock, predicate::*};

// new module to include types based on proto file
pub mod dataquery {
    tonic::include_proto!("dataquery");
}


fn create_get_data_request() -> GetDataRequest {
    let req = GetDataRequest {
        user_id: "victor.ty.ho".to_owned(),
        user_token: "wqeadsAATYGDGDqwwqeadsAATYGDGDqw".to_owned(),
        data_id:  "ZN".to_owned(),
        data_type: "snap.NKY".to_owned(),
        return_type: 0,  
    };
    return req;
}

fn create_meta_data_request() -> MetadataRequest {
    let req = MetadataRequest {
        user_id: "victor.ty.ho".to_owned(),
        user_token: "wqeadsAATYGDGDqwwqeadsAATYGDGDqw".to_owned(),
        data_id:  "JGB10Y".to_owned(),
        data_type: "snap.TSE".to_owned(),
    };
    return req;
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut client = DataQueryClient::connect("http://[::1]:9999").await?;

    // #1 RPC call to get_data()  
    let data_req = tonic::Request::new(create_get_data_request());
    let response = client.get_data(data_req).await?;
    println!("get_data RESPONSE={:?}", response);

    // #2 RPC call to inspect_metadata()
    let meta_req = tonic::Request::new(create_meta_data_request());
    let response2 = client.inspect_metadata(meta_req).await?;
    println!("inspect_metadata RESPONSE={:?}", response2);

    Ok(())
}


//////////////////////////////////////////////////////////////////////
// Unit Tests (live in same file as code)
#[cfg(test)]
mod client_tests {
    use super::*;

    #[test]
    fn get_data_req_test() {
        let req = create_get_data_request();
        assert!(!req.user_id.is_empty());
    }

    #[test]
    fn meta_data_req_test() {
        let req = create_meta_data_request();
        assert!(!req.user_id.is_empty());
    }
}