import csv
from models.sale import Sale

class ReportGenerator:
    def __init__(self,filepath='reports/csv_report/sales_report.csv'):
        self.filepath = filepath

    def generate_report(self):
        sales = Sale.get_all_sales()
        try:
            with open(self.filepath,'w',newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Sale ID","Product ID","Quantity","Price","Date"])
                for sale in sales:
                    writer.writerow([
                        sale.id,
                        sale.product_id,
                        sale.quantity,
                        sale.price,
                        sale.date.strftime('%Y-%m-%d %H-%M-%S')
                    ])
                print(f"Report generated: {self.filepath}")
        except IOError as e:
            print(f"Error generating report: {e}")

report = ReportGenerator()
print(report.generate_report())