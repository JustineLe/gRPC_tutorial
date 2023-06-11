import grpc
from concurrent import futures
import message_pb2_grpc as mes_pb2_grpc
import message_pb2 as mes_pb2
from unary_client import validate


class MessageService(mes_pb2_grpc.MessageServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):

        # get the string from the incoming request
        message = request.message
        validate("call")
        result = f'Hello I am up and running received "{message}" message from you'
        result = {'message': result, 'received': True}

        return mes_pb2.DataResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mes_pb2_grpc.add_MessageServicer_to_server(MessageService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
