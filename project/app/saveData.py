from app.models import StudentDetails
import json
class SaveData:
    def saveDataToDb(self,request):
        try:
            print(request)
            payload = request.data
            print(json.dumps(payload,indent=4))
            payload = payload.get('data')
            print(json.dumps(payload,indent=4))
            #Write code for calculating total marks

            for i in payload:
                print(i)
                total = i.get('subject1')+i.get('subject2')+i.get('subject3')
                
                StudentDetails.objects.create(
                    name=i.get('name'),
                    Subject1=i.get('subject1'),
                    Subject2= i.get('subject2'),
                    Subject3 = i.get('subject3'),
                    total=total,
                    percentage=total/3
                )
        except Exception as e:
            raise Exception(str(e))
