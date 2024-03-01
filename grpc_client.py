import grpc

# import the generated classes
import insultingServer_pb2
import insultingServer_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = insultingServer_pb2_grpc.InsultingServiceStub(channel)

# create a valid request message
insult = insultingServer_pb2.Insult(insult='Moc', severity=0.1)
stub.AddInsult(insult)

insult = insultingServer_pb2.Insult(insult='Mocoloco', severity=0.5)
stub.AddInsult(insult)

insult = insultingServer_pb2.Insult(insult='Mocoloquito', severity=1.0)
stub.AddInsult(insult)

# create a valid request message
empty = insultingServer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
response = stub.GetInsults(empty)
print(response.value)

# create a valid request message
empty = insultingServer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
response = stub.InsultMe(empty)
print(response.insult_name)

insult = insultingServer_pb2.InsultName(insult_name='Mocoloco')
response = stub.GetSeverity(insult)
print(response.value)
