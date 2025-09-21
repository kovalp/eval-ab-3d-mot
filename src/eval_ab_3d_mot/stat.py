"""."""

import os

import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt


NUM_SAMPLE_POINTS = 41.0


class Stat:
    """
    Utility class to load data.
    """

    def __init__(self, t_sha, cls, suffix, dump):
        """
        Constructor, initializes the object given the parameters.
        """

        # init object data
        self.mota = 0
        self.motp = 0
        self.F1 = 0
        self.precision = 0
        self.fp = 0
        self.fn = 0
        self.sMOTA = 0

        self.mota_list = list()
        self.motp_list = list()
        self.sMOTA_list = list()
        self.f1_list = list()
        self.precision_list = list()
        self.fp_list = list()
        self.fn_list = list()
        self.recall_list = list()

        self.t_sha = t_sha
        self.cls = cls
        self.suffix = suffix
        self.dump = dump

    def update(self, data):
        self.mota += data['mota']
        self.motp += data['motp']
        self.F1 += data['F1']
        # self.moda += data['moda']
        # self.modp += data['modp']
        self.precision += data['precision']
        self.fp += data['fp']
        self.fn += data['fn']
        self.sMOTA += data['sMOTA']

        self.mota_list.append(data['mota'])
        self.sMOTA_list.append(data['sMOTA'])
        self.motp_list.append(data['motp'])
        self.f1_list.append(data['F1'])
        self.precision_list.append(data['precision'])
        self.fp_list.append(data['fp'])
        self.fn_list.append(data['fn'])
        self.recall_list.append(data['recall'])

    def output(self):
        self.sAMOTA = self.sMOTA / (NUM_SAMPLE_POINTS - 1)
        self.amota = self.mota / (NUM_SAMPLE_POINTS - 1)
        self.amotp = self.motp / (NUM_SAMPLE_POINTS - 1)

    def print_summary(self):
        summary = ''

        summary += ('evaluation: average over recall').center(80, '=') + '\n'
        summary += ' sAMOTA  AMOTA  AMOTP \n'

        summary += '{:.4f} {:.4f} {:.4f}\n'.format(self.sAMOTA, self.amota, self.amotp)
        summary += '=' * 80

        print(summary, file=self.dump)

        return summary

    def plot_over_recall(self, data_list, title, y_name, save_path):
        # add extra zero at the end
        largest_recall = self.recall_list[-1]
        extra_zero = np.arange(largest_recall, 1, 0.01).tolist()
        len_extra = len(extra_zero)
        y_zero = [0] * len_extra

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(np.array(self.recall_list + extra_zero), np.array(data_list + y_zero))
        # ax.set_title(title, fontsize=20)
        ax.set_ylabel(y_name, fontsize=20)
        ax.set_xlabel('Recall', fontsize=20)
        ax.set_xlim(0.0, 1.0)
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        plt.tight_layout()
        if y_name in ['sMOTA', 'MOTA', 'MOTP', 'F1', 'Precision']:
            ax.set_ylim(0.0, 1.0)
        else:
            ax.set_ylim(0.0, max(data_list))

        if y_name in ['MOTA', 'F1']:
            max_ind = np.argmax(np.array(data_list))
            # print(max_ind)
            plt.axvline(self.recall_list[max_ind], ymax=data_list[max_ind], color='r')
            plt.plot(self.recall_list[max_ind], data_list[max_ind], 'or', markersize=12)
            plt.text(
                self.recall_list[max_ind] - 0.05,
                data_list[max_ind] + 0.03,
                '%.2f' % (data_list[max_ind] * 100),
                fontsize=20,
            )
        fig.savefig(save_path)
        plt.close()
        # zxc

    def plot(self):
        save_dir = os.path.join('./results/KITTI', self.t_sha)

        self.plot_over_recall(
            self.mota_list,
            'MOTA - Recall Curve',
            'MOTA',
            os.path.join(save_dir, 'MOTA_recall_curve_%s_%s.pdf' % (self.cls, self.suffix)),
        )
        self.plot_over_recall(
            self.sMOTA_list,
            'sMOTA - Recall Curve',
            'sMOTA',
            os.path.join(save_dir, 'sMOTA_recall_curve_%s_%s.pdf' % (self.cls, self.suffix)),
        )
        self.plot_over_recall(
            self.motp_list,
            'MOTP - Recall Curve',
            'MOTP',
            os.path.join(save_dir, 'MOTP_recall_curve_%s_%s.pdf' % (self.cls, self.suffix)),
        )
        self.plot_over_recall(
            self.f1_list,
            'F1 - Recall Curve',
            'F1',
            os.path.join(save_dir, 'F1_recall_curve_%s_%s.pdf' % (self.cls, self.suffix)),
        )
        self.plot_over_recall(
            self.fp_list,
            'False Positive - Recall Curve',
            'False Positive',
            os.path.join(save_dir, 'FP_recall_curve_%s_%s.pdf' % (self.cls, self.suffix)),
        )
        self.plot_over_recall(
            self.fn_list,
            'False Negative - Recall Curve',
            'False Negative',
            os.path.join(save_dir, 'FN_recall_curve_%s_%s.pdf' % (self.cls, self.suffix)),
        )
        self.plot_over_recall(
            self.precision_list,
            'Precision - Recall Curve',
            'Precision',
            os.path.join(save_dir, 'precision_recall_curve_%s_%s.pdf' % (self.cls, self.suffix)),
        )

