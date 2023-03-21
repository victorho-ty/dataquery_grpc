use tonic::{transport::Server, Request, Response, Status};

// Reference: https://github.com/letsgetrusty/grpc_example


// import tonic generated based on proto definitions
use dataquery::data_query_server::{DataQuery, DataQueryServer};
use dataquery::{GetDataRequest, GetDataResponse, MetadataRequest, MetadataResponse};

// new module to include types based on proto file
pub mod dataquery {
    tonic::include_proto!("dataquery");
}

#[derive(Debug, Default)]
pub struct DataQueryService {}



fn verify_user_token(token: &String) -> bool { 
    return !token.is_empty();    
}


// async_trait for the function to be async
#[tonic::async_trait]
impl DataQuery for DataQueryService {

    async fn get_data(&self, request: Request<GetDataRequest>) -> Result<Response<GetDataResponse>, Status> {
        let req: GetDataRequest = request.into_inner();
        let _is_valid_user = verify_user_token(&req.user_token);

        println!("[{}] Called get_data. Data({}, {}) ", req.user_id, req.data_id, req.data_type);

        let reply = GetDataResponse {
            response_code: 200,
            data_payload: format!("Sent to [{}]. Data Payload.", req.user_id).into(),
        };

        Ok(Response::new(reply))
    }

    async fn inspect_metadata(&self, request: Request<MetadataRequest>) -> Result<Response<MetadataResponse>, Status> {
        let req: MetadataRequest = request.into_inner();
        let _is_valid_user = verify_user_token(&req.user_token);

        println!("[{}] Called inspect_metadata. Data({}, {}) ", req.user_id, req.data_id, req.data_type);

        let reply = MetadataResponse {
            response_code: 200,
            meta_data: vec!["mongoDB".to_owned(), "01-04-2013".to_owned(), "03-10-2023".to_owned()],
        };

        Ok(Response::new(reply))
    }
}


#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = "[::1]:9999".parse()?;
    let data_service = DataQueryService::default();

    Server::builder()
        .add_service(DataQueryServer::new(data_service))
        .serve(addr)
        .await?;

    Ok(())
}


//////////////////////////////////////////////////////////////////////
// Tests

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn verify_user_token_test() {
        let res1: bool = verify_user_token(&"valid token".to_string());
        assert_eq!(res1, true);

        let res2: bool = verify_user_token(&"".to_string());
        assert_eq!(res2, false);
    }
}