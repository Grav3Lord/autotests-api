from concurrent import futures  # Импорт пула потоков для асинхронного выполнения

import grpc  # Импорт библиотеки gRPC

import course_service_pb2  # Сгенерированные классы для работы с gRPC-сообщениями
import course_service_pb2_grpc  # Сгенерированный класс для работы с сервисом

class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):

    def GetCourse(self, request, context):
        print(f"Получен запрос к методу GetCourse от {request.course_id}")

        return course_service_pb2.GetCourseResponse(course_id=request.course_id, title="Автотесты API",
                                                    description="Будем изучать написание API автотестов")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC сервер запущен на localhost:50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()