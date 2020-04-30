import random
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt

class Charts:
    @staticmethod
    def get_chart(xlist, ylist, labelslist):
        plt.switch_backend('Agg')
        
        fig, ax = plt.subplots()
        ax.set_title("Taxa de crescimento diário de óbitos")
        ax.set_xlabel("Dia/Mês")
        ax.set_ylabel("Óbitos / Óbitos dia anterior (%)")
        ax.grid()

        for x, y, l in zip(xlist, ylist, labelslist):
            line, = ax.plot(x, y, '.-', label=l)
            # ax.bar(x, y, label=l)

        for label in ax.get_xaxis().get_ticklabels()[::2]:
            label.set_visible(False)
        fig.autofmt_xdate()

        # other legends
        # https://stackoverflow.com/questions/4700614/how-to-put-the-legend-out-of-the-plot

        ax.legend(loc="upper right")

        buffer = BytesIO()
        fig.savefig(buffer, format="png", transparent=True)
        return buffer.getvalue()

    @staticmethod
    def get_pie_chart(sizes,labels):
        plt.switch_backend('Agg')

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        buffer = BytesIO()
        fig.savefig(buffer, format="png", transparent=True)
        return buffer.getvalue()