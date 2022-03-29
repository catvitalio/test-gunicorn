from rest_framework import views

from openpyxl import Workbook


class NewView(views.APIView):
    def get(self, request):
        wb = Workbook()
        sheet = wb.active

        while True:
            sheet.append(('lala', 'lala', 'lalala', '12323dsa', '1n2u3indkjsan', '132awds123fase32rferyfuy34hjr2'))