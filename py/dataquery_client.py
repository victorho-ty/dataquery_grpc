import grpc
import dataquery_pb2
import dataquery_pb2_grpc


###########################################################
# Entry Point Run
def run_client():
    grpc_server_str = "localhost:9999"

    with grpc.insecure_channel(grpc_server_str) as channel:
        stub = dataquery_pb2_grpc.DataQueryStub(channel)

        user_id = "victor.ty.ho"
        user_token = "wqeadsAATYGDGDqwwqeadsAATYGDGDqw"
        data_id = "ZN"
        data_type = "snap.NKY"
        return_type = 0

        # 1. Client calls GetData()
        get_data_resp = stub.GetData(dataquery_pb2.GetDataRequest(user_id=user_id,
                                                                  user_token=user_token,
                                                                  data_id=data_id,
                                                                  data_type=data_type,
                                                                  return_type=return_type))
        print("Python Client, GetData response. Code= %d, Payload= %s" %
              (get_data_resp.response_code, get_data_resp.data_payload))

        # 2. Client calls InspectMetaData()
        meta_data_resp = stub.InspectMetadata(dataquery_pb2.MetadataRequest(user_id=user_id,
                                                                            user_token=user_token,
                                                                            data_id=data_id,
                                                                            data_type=data_type))
        print("Python Client, InspectMetadata response. Code= %d, MetaData= %s" %
              (meta_data_resp.response_code, str(meta_data_resp.meta_data)))


if __name__ == "__main__":
    run_client()