from src.view.http_types.http_response import HttpResponse
import traceback

class ErrorHandler:

    def __init__(self, exception):
        self.response = self.handle_error(exception)

    def handle_error(self, error):
        if type(error).__name__ == 'BadRequestException':
            print('chegou aqui')
            return HttpResponse(403, {'response': f'{str(error)} {error.errors}'})
        if type(error).__name__ == 'EntityAlreadyExistsException':
            return HttpResponse(403, {'response': str(error)})
        else:
            print(traceback.format_exc())
            return HttpResponse(500, {'response': 'Ocorreu um erro'})
        
