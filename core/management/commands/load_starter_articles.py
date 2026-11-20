"""Create the four starter blog articles as DRAFTS (skips any that already exist).

Usage:  python manage.py load_starter_articles            (as drafts)
        python manage.py load_starter_articles --publish  (published)

Drafts are only visible to logged-in admins. Review and edit them in the admin
panel (Blog posts), then set Status to "Published".
"""
from django.core.management.base import BaseCommand
from django.utils import timezone

from core.models import BlogPost

ARTICLES = [
    {
        'title': 'When Does a Growing Business Need a Virtual CFO?',
        'category': 'business',
        'cover_image': 'images/site/blog-featured.jpg',
        'summary': 'Seven clear signs that your business has outgrown basic bookkeeping, and how a Virtual CFO fills the gap without the cost of a full-time finance head.',
        'body': """Most businesses start with an accountant who records transactions and files returns. That is essential work, but it looks backwards: it tells you what already happened. As a business grows, the owner needs someone who looks forward: planning cash, setting targets, spotting risks early and turning numbers into decisions. That is the role of a CFO.

The problem is that a full-time, experienced CFO is expensive, and many growing businesses do not need one five days a week. A **Virtual CFO** gives you the same strategic finance leadership on a part-time or retainer basis.

## Seven signs it is time

1. **You find out about cash problems too late.** Salaries, GST payments or supplier dues arrive and the bank balance is lower than you expected.
2. **You do not get a monthly MIS report.** If you cannot see last month's profit, margins and receivables by the 10th of the following month, you are making decisions on instinct.
3. **Sales are growing but profit is not.** Higher turnover with flat or falling profit usually points to pricing, cost or working-capital issues that need analysis.
4. **Your bank or investors ask for projections you cannot produce.** Loan renewals, new credit limits and fundraising all need budgets, forecasts and a clear financial story.
5. **You spend your evenings on spreadsheets.** If the owner is the finance department, growth slows because strategic time goes into routine work.
6. **Receivables keep piling up.** Customers paying in 90 days while you pay suppliers in 30 is a common reason profitable businesses run short of cash.
7. **You are planning something big.** A new plant, a new branch, an acquisition or an IPO all need financial planning well before the decision is made.

## What a Virtual CFO actually does

- Builds an annual **budget** and tracks actual results against it every month
- Prepares **cash flow forecasts** so shortfalls are visible weeks in advance
- Sets up a monthly **MIS** with the few numbers that matter for your business
- Reviews **pricing, margins and costs** by product, customer or branch
- Strengthens **internal controls** so errors and leakages are caught early
- Supports conversations with **banks and investors**
- Works alongside your existing accountant and auditor rather than replacing them

## Virtual CFO or full-time CFO?

A full-time CFO makes sense when the finance function is large enough to need daily leadership: multiple entities, a big finance team, or a listed company. Until then, a Virtual CFO usually gives better value: senior expertise when you need it, a fixed monthly cost, and no long hiring process.

## How to get started

Start with a short review of your current numbers: last year's accounts, the latest month's figures, and your receivables and payables. From there, a Virtual CFO can tell you which two or three changes will make the biggest difference first. Usually that means a monthly MIS, a 13-week cash forecast and a budget for the year ahead.

If two or more of the signs above sound familiar, it is worth having that first conversation.""",
    },
    {
        'title': 'Monthly GST Compliance Checklist for Small and Medium Businesses',
        'category': 'gst_tax',
        'cover_image': 'images/site/blog-gst.jpg',
        'summary': 'A practical month-by-month routine for GST returns, input tax credit and records, so you avoid late fees, interest and lost credit.',
        'body': """GST compliance is not difficult when it follows a routine. Most penalties, interest and lost input tax credit (ITC) come from doing things at the last minute or skipping reconciliations. Here is a simple monthly checklist that keeps a small or medium business on track.

## Week 1: close last month's books

- Make sure every **sales invoice** for the month is recorded, including credit and debit notes.
- Record all **purchase invoices** and expense bills with the supplier's GSTIN.
- If your turnover requires **e-invoicing**, confirm every B2B invoice has an IRN (Invoice Reference Number) from the IRP portal.
- Check that **e-way bills** were generated for goods movements where required.

## Before the GSTR-1 due date: report your sales

- Monthly filers file **GSTR-1** by the 11th of the following month.
- Businesses under the **QRMP scheme** file GSTR-1 quarterly, and can use the optional IFF to upload B2B invoices in the first two months so their customers can claim credit on time.
- Double-check customer GSTINs, place of supply and HSN codes. Errors here affect your customers' credit and lead to follow-up questions.
- If something is wrong after filing, correct it through **GSTR-1A** or in a later return rather than ignoring it, because the liability shown in GSTR-3B is increasingly taken directly from GSTR-1.

## Around the 14th: reconcile your input tax credit

- Download **GSTR-2B**, the auto-drafted statement of credit available to you.
- Use the **Invoice Management System (IMS)** on the GST portal to accept, reject or keep pending the invoices suppliers have uploaded.
- Match GSTR-2B against your purchase register. Claim credit only for invoices that appear in GSTR-2B and that you have actually received.
- Follow up with suppliers whose invoices are missing. In most cases you cannot claim credit until the supplier reports the invoice.

## Before the GSTR-3B due date: pay and file

- Monthly filers file **GSTR-3B** by the 20th of the following month.
- QRMP filers pay tax monthly through **PMT-06** by the 25th, and file GSTR-3B quarterly by the 22nd or 24th depending on their state (Gujarat falls in the 22nd group).
- Pay the tax in full and on time. Late payment attracts **interest at 18% per year**, and late filing attracts a **late fee per day** of delay.

## Every month: keep credit safe

- **Pay suppliers within 180 days** of the invoice date. If you do not, the related ITC must be reversed (it can be re-claimed after payment).
- Reverse ITC on items where credit is blocked, such as many personal-use and certain vehicle expenses.
- Keep invoices, e-way bills and payment proofs organised. Notices often arrive years later.

## Every year: the deadlines people forget

- ITC for a financial year must be claimed by **30 November** of the following year (or the date of filing the annual return, if earlier). Missed invoices after that date are lost credit.
- Plan the **annual return (GSTR-9)** and, where applicable, the **reconciliation statement (GSTR-9C)** well before the due date.

## A simple habit that prevents most problems

Block two fixed slots in your calendar each month: one after the 14th to reconcile GSTR-2B, and one a few days before your GSTR-3B due date to review, pay and file. Businesses that follow this routine rarely face surprises.

*Note: GST due dates, thresholds and procedures change through government notifications and portal updates. Always confirm the current dates on the GST portal or with your advisor before filing.*""",
    },
    {
        'title': '7 Practical Ways to Improve Your Business Cash Flow',
        'category': 'cash_flow',
        'cover_image': 'images/site/blog-cashflow.jpg',
        'summary': 'Profitable businesses still run out of cash. These seven steps help you collect faster, plan better and keep more money working in the business.',
        'body': """Profit and cash are not the same thing. A business can show a healthy profit on paper and still struggle to pay salaries and suppliers, because the cash is stuck with customers or in stock. Improving cash flow is usually about a handful of disciplined habits, not one big change.

## 1. Know your cash conversion cycle

Your **cash conversion cycle** shows how many days money is tied up between paying for inputs and collecting from customers:

**Inventory days + Receivable days (DSO) - Payable days (DPO)**

If this number is 90, every rupee spent today comes back in about three months. Reducing it by even 15 days can release a large amount of cash without borrowing.

## 2. Invoice immediately and accurately

Every day an invoice is delayed is a day added to collection. Raise invoices as soon as goods are delivered or milestones are completed, and make sure GSTIN, PO numbers and amounts are correct. Customers often hold payment over small errors.

## 3. Follow up before the due date, not after

- Send a polite reminder a few days **before** payment is due.
- Call on the due date if payment has not arrived.
- Review an **ageing report** every week: which customers are 30, 60 and 90+ days overdue.
- Decide in advance when to pause further supplies to customers who stay overdue.

## 4. Set clear credit terms for each customer

Not every customer deserves the same credit period. Set credit limits and terms based on payment history, and review them every quarter. Offering a small discount for early payment can be cheaper than funding the receivable with a bank loan.

## 5. Manage payables, and pay MSMEs on time

Use the full credit period your suppliers allow, but do not delay beyond it: it damages relationships and pricing. Pay particular attention to suppliers registered as **micro or small enterprises**. Under Section 43B(h) of the Income Tax Act, payments due to them must generally be made within 15 days, or up to 45 days where there is a written agreement, otherwise the expense may not be allowed as a deduction until it is paid.

## 6. Keep inventory lean

Slow-moving stock is cash sitting on shelves. Identify items that have not moved in 90 days, stop reordering them, and clear them out even at a lower margin. Reorder fast-moving items based on actual consumption rather than habit.

## 7. Forecast cash 13 weeks ahead

A simple **13-week cash forecast** lists expected receipts and payments week by week: collections, salaries, rent, GST, loan EMIs and supplier payments. Updated every week, it shows shortfalls well in advance, so you can arrange funds, push collections or reschedule purchases calmly instead of in a crisis.

## Where to start

Pick two actions this month: a weekly ageing review and a 13-week cash forecast. Together they usually show quickly where cash is stuck and how much can be released.""",
    },
    {
        'title': '10 KPIs Every Business Owner Should Track Monthly',
        'category': 'kpi_growth',
        'cover_image': 'images/site/blog-kpi.jpg',
        'summary': 'You do not need fifty reports. These ten numbers, reviewed every month, give a clear picture of profitability, cash and growth.',
        'body': """Many owners receive long reports and still do not know how the business is really doing. The answer is not more data; it is a short list of the right numbers, reviewed every month and compared with last month, last year and the budget.

## Profitability

1. **Revenue growth.** This month and year-to-date, compared with the same period last year and with your budget. Look at it by product, branch or customer group, not just in total.
2. **Gross margin %.** (Revenue - direct costs) / revenue. A falling gross margin is often the earliest warning of pricing pressure or rising input costs.
3. **Net profit margin %.** What remains after all expenses. Track the trend over several months rather than reacting to a single month.
4. **Break-even revenue.** The monthly sales needed to cover all fixed costs. Knowing it makes hiring, rent and expansion decisions much clearer.

## Cash and working capital

5. **Cash balance and 13-week forecast.** Cash in the bank today, and expected cash at the lowest point in the coming weeks.
6. **Receivable days (DSO).** (Receivables / revenue) x days in the period. If this keeps rising, customers are effectively borrowing from you.
7. **Payable days (DPO) and inventory days.** Together with DSO, these give your cash conversion cycle: how long money is tied up in operations.

## Financial health

8. **Current ratio.** Current assets / current liabilities. Below 1 means short-term obligations exceed short-term resources, a signal to act early.
9. **Debt service coverage.** Whether operating cash flow comfortably covers loan repayments and interest. Banks look closely at this number.

## Growth quality

10. **Customer concentration.** The share of revenue from your top one, five and ten customers. If one customer is more than a quarter of your sales, losing them would be a serious risk.

## Making KPIs useful

- **Keep it to one page.** If a number does not lead to a decision, drop it.
- **Same day every month.** Aim to have the KPI sheet ready by the 10th of the following month.
- **Always show a comparison:** budget, last month and the same month last year.
- **Assign an owner** to every KPI who explains the movement and the action being taken.
- **Use a dashboard.** A simple visual dashboard makes trends obvious at a glance and saves hours of manual reporting.

## Where to start

Begin with five: revenue growth, gross margin, cash forecast, receivable days and customer concentration. Once those are reviewed reliably every month, add the rest.""",
    },
]


class Command(BaseCommand):
    help = 'Create the starter blog articles as drafts (existing titles are skipped).'

    def add_arguments(self, parser):
        parser.add_argument('--publish', action='store_true', help='Publish the articles instead of saving drafts.')

    def handle(self, *args, **options):
        status = BlogPost.STATUS_PUBLISHED if options['publish'] else BlogPost.STATUS_DRAFT
        created = 0
        for article in ARTICLES:
            if BlogPost.objects.filter(title=article['title']).exists():
                self.stdout.write(f"Skipped (already exists): {article['title']}")
                continue
            BlogPost.objects.create(status=status, published_at=timezone.now(), **article)
            created += 1
            self.stdout.write(self.style.SUCCESS(f"Created ({status}): {article['title']}"))
        self.stdout.write(f'{created} new article(s) created as {status}. Manage them in the admin panel under Blog posts.')
