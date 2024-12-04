# run again.  Do not edit this file unless you know what you are doing.
import platform

from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import Qt

from videotrans.configure import config
from videotrans.configure.config import box_lang
from videotrans.recognition import RECOGN_NAME_LIST


class Ui_recogn(object):
    def setupUi(self, recogn):
        self.has_done = False
        self.error_msg = ""
        recogn.setObjectName("recogn")
        recogn.setMinimumSize(1000, 500)

        self.centralwidget = QtWidgets.QWidget(recogn)
        self.centralwidget.setObjectName("centralwidget")


        self.shibie_out_path = None

        # 语音识别
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(recogn)

        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.shibie_widget = QtWidgets.QVBoxLayout()
        self.shibie_widget.setObjectName("shibie_widget")
        self.verticalLayout_3.addLayout(self.shibie_widget)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")


        self.label_3 = QtWidgets.QLabel()
        self.label_3.setObjectName("label_3")
        self.shibie_language = QtWidgets.QComboBox()
        self.shibie_language.setMinimumSize(QtCore.QSize(100, 30))
        self.shibie_language.setObjectName("shibie_language")


        self.is_cuda = QtWidgets.QCheckBox()
        self.is_cuda.setObjectName("is_cuda")
        self.is_cuda.setText("启用CUDA?" if config.defaulelang == 'zh' else 'Enable CUDA?')
        # 如果是 MAc系统则隐藏
        if platform.system() == 'Darwin':
            self.is_cuda.setVisible(False)


        self.shibie_label = QtWidgets.QPushButton()
        self.shibie_label.setText("语音识别\u2193")
        self.shibie_label.setStyleSheet("""background-color:transparent""")
        self.shibie_label.setCursor(Qt.PointingHandCursor)
        self.shibie_label.setToolTip(
            '当faster-whisper时，可点击设置详细识别参数' if config.defaulelang == 'zh' else 'Click to set detailed recognition parameters when using faster-whisper')
        self.shibie_recogn_type = QtWidgets.QComboBox()
        self.shibie_recogn_type.setMinimumSize(QtCore.QSize(150, 30))
        self.shibie_recogn_type.setObjectName("shibie_recogn_type")



        label_model=QtWidgets.QLabel()
        label_model.setText('选择模型' if config.defaulelang=='zh' else 'Select model')

        self.shibie_model = QtWidgets.QComboBox()
        self.shibie_model.setMinimumSize(QtCore.QSize(100, 30))
        self.shibie_model.setObjectName("shibie_model")

        self.shibie_split_type = QtWidgets.QComboBox()
        self.shibie_split_type.addItems(
            [config.transobj['whisper_type_all'],
             config.transobj['whisper_type_avg']]
        )
        self.shibie_split_type.setToolTip(config.transobj['fenge_tips'])


        split_label=QtWidgets.QLabel()
        split_label.setText('分割模式' if config.defaulelang=='zh' else 'Split mode')

        self.equal_split_time= QtWidgets.QLineEdit()
        self.equal_split_time.setToolTip('每段分割时长/单位秒' if config.defaulelang=='zh' else 'Duration of each segment/second')
        self.equal_split_time.setText(str(config.settings.get('interval_split',10)))
        self.equal_split_time_label= QtWidgets.QLabel()
        self.equal_split_time_label.setText('秒' if config.defaulelang=='zh' else 'Sec')
        self.equal_split_time.setVisible(False)
        self.equal_split_time_label.setVisible(False)

        self.equal_split_layout= QtWidgets.QHBoxLayout()
        self.equal_split_layout.addWidget(self.equal_split_time)
        self.equal_split_layout.addWidget(self.equal_split_time_label)

        lable_out=QtWidgets.QLabel()
        lable_out.setText('输出字幕格式' if config.defaulelang=='zh' else 'Subtitle format:')
        self.out_format=QtWidgets.QComboBox()
        self.out_format.setMinimumSize(QtCore.QSize(100, 35))
        self.out_format.addItems([
            "srt",
            "ass",
            "vtt"
        ])



        self.shibie_startbtn = QtWidgets.QPushButton()
        self.shibie_startbtn.setMinimumSize(QtCore.QSize(200, 35))
        self.shibie_startbtn.setObjectName("shibie_startbtn")
        self.shibie_startbtn.setCursor(Qt.PointingHandCursor)

        self.shibie_stop = QtWidgets.QPushButton()
        self.shibie_stop.setFixedWidth(80)
        self.shibie_stop.setDisabled(True)
        self.shibie_stop.setText("停止" if config.defaulelang=='zh' else 'Stop')
        self.shibie_stop.setCursor(Qt.PointingHandCursor)

        self.horizontalLayout.addStretch()

        self.horizontalLayout.addWidget(self.label_3)
        self.horizontalLayout.addWidget(self.shibie_language)
        self.horizontalLayout.addWidget(self.shibie_label)
        self.horizontalLayout.addWidget(self.shibie_recogn_type)
        self.horizontalLayout.addWidget(label_model)
        self.horizontalLayout.addWidget(self.shibie_model)
        self.horizontalLayout.addWidget(split_label)
        self.horizontalLayout.addWidget(self.shibie_split_type)
        self.horizontalLayout.addLayout(self.equal_split_layout)
        self.horizontalLayout.addWidget(lable_out)
        self.horizontalLayout.addWidget(self.out_format)
        self.horizontalLayout.addStretch()

        h4= QtWidgets.QHBoxLayout()

        self.label_cjklinenums = QtWidgets.QLabel()
        self.label_cjklinenums.setObjectName("label_cjklinenums")
        self.label_cjklinenums.setText(
            '中日韩单行字符' if config.defaulelang == 'zh' else 'CJK line length')

        self.cjklinenums = QtWidgets.QSpinBox()
        self.cjklinenums.setMinimum(5)
        self.cjklinenums.setMinimumWidth(90)
        self.cjklinenums.setMaximum(100)
        self.cjklinenums.setObjectName("cjklinenums")
        self.cjklinenums.setToolTip("中日韩字幕单行字符数" if config.defaulelang=='zh' else 'Chinese/Japanese/Korean line length')
        self.cjklinenums.setValue(int(config.settings.get('cjk_len', 20)))

        self.label_othlinenums = QtWidgets.QLabel()
        self.label_othlinenums.setObjectName("label_othlinenums")
        self.label_othlinenums.setText(
            '其他语言' if config.defaulelang == 'zh' else 'Other line length')


        self.othlinenums = QtWidgets.QSpinBox()
        self.othlinenums.setToolTip("其他语言字幕单行字符数" if config.defaulelang=='zh' else 'Other language line length')
        self.othlinenums.setMinimum(5)
        self.othlinenums.setMaximum(100)
        self.othlinenums.setMinimumWidth(90)
        self.othlinenums.setObjectName("othlinenums")
        self.othlinenums.setValue(int(config.settings.get('other_len', 60)))

        self.rephrase=QtWidgets.QCheckBox()
        self.rephrase.setText('重新断句' if config.defaulelang=='zh' else 'Rephrase')
        self.rephrase.setToolTip('当选择faster/openai-whisper/Deepgram渠道时时有效' if config.defaulelang=='zh' else 'Valid when selecting the fast/openai-whisper/Deep program')

        self.remove_noise=QtWidgets.QCheckBox()
        self.remove_noise.setText('降噪处理' if config.defaulelang=='zh' else 'Noise reduction')
        self.remove_noise.setToolTip('若选中将从modelscope.cn下载模型做音频降噪处理，比较耗时' if config.defaulelang=='zh' else 'Select to perform noise reduction processing from modelscope.cn, which takes a long time')

        h4.addStretch()
        h4.addWidget(self.shibie_startbtn)
        h4.addWidget(self.shibie_stop)
        h4.addWidget(self.is_cuda)
        h4.addWidget(self.label_cjklinenums)
        h4.addWidget(self.cjklinenums)
        h4.addWidget(self.label_othlinenums)
        h4.addWidget(self.othlinenums)
        h4.addWidget(self.rephrase)
        h4.addWidget(self.remove_noise)

        h4.addStretch()

        self.verticalLayout_3.addLayout(self.horizontalLayout)


        # 语音调整行
        # 语音识别高级行
        self.hfaster_layout = QtWidgets.QHBoxLayout()
        self.threshold_label = QtWidgets.QLabel()
        self.threshold_label.setText('threshold' if config.defaulelang != 'zh' else '语音识别阈值')
        self.threshold_label.setVisible(False)
        self.threshold = QtWidgets.QLineEdit()
        self.threshold.setPlaceholderText('200ms')
        self.threshold.setMaximumWidth(80)
        self.threshold.setVisible(False)
        self.threshold.setToolTip(
            '表示语音的概率阈值，VAD 会输出每个音频片段的语音概率。\n高于该值的概率被认为是语音（SPEECH），低于该值的概率被认为是静音或背景噪音。默认值为 0.5，这在大多数情况下是适用的。\n但针对不同的数据集，你可以调整这个值以更精确地区分语音和噪音。如果你发现误判太多，可以尝试将其调高到 0.6 或 0.7；\n如果语音片段丢失过多，则可以降低至 0.3 或 0.4。' if config.defaulelang == 'zh' else 'Threshold for speech detection')
        self.threshold.setText(str(config.settings.get('threshold', 0.5)))
        self.hfaster_layout.addWidget(self.threshold_label)
        self.hfaster_layout.addWidget(self.threshold)
        self.hfaster_layout.addStretch()

        self.min_speech_duration_ms_label = QtWidgets.QLabel()
        self.min_speech_duration_ms_label.setText(
            'min_speech_duration_ms' if config.defaulelang != 'zh' else '最小语音持续毫秒')
        self.min_speech_duration_ms_label.setVisible(False)
        self.min_speech_duration_ms = QtWidgets.QLineEdit()
        self.min_speech_duration_ms.setPlaceholderText('200ms')
        self.min_speech_duration_ms.setMaximumWidth(80)
        self.min_speech_duration_ms.setVisible(False)
        self.min_speech_duration_ms.setText(str(config.settings.get('min_speech_duration_ms', 250)))
        self.min_speech_duration_ms.setToolTip(
            '最小语音持续时间，单位：毫秒。\n如果检测到的语音片段长度小于这个值，则该语音片段会被丢弃。目的是去除一些短暂的非语音声音或噪音。\n默认值为 250 毫秒，适合大多数场景。你可以根据需要调整，如果语音片段过短容易被误判为噪音，可以增加该值，\n例如设置为 500 毫秒' if config.defaulelang == 'zh' else 'Minimum speech duration (ms)')
        self.hfaster_layout.addWidget(self.min_speech_duration_ms_label)
        self.hfaster_layout.addWidget(self.min_speech_duration_ms)
        self.hfaster_layout.addStretch()


        self.min_silence_duration_ms_label = QtWidgets.QLabel()
        self.min_silence_duration_ms_label.setText(
            'min_silence_duration_ms' if config.defaulelang != 'zh' else '最小静音持续毫秒')
        self.min_silence_duration_ms_label.setVisible(False)
        self.min_silence_duration_ms = QtWidgets.QLineEdit()
        self.min_silence_duration_ms.setPlaceholderText('200ms')
        self.min_silence_duration_ms.setMaximumWidth(80)
        self.min_silence_duration_ms.setVisible(False)
        self.min_silence_duration_ms.setText(str(config.settings.get('min_silence_duration_ms', 2000)))
        self.min_silence_duration_ms.setToolTip(
            '最小静音持续时间，单位：毫秒。\n当检测到语音结束后，会等待的静音时间。如果静音持续时间超过该值，才会分割语音片段。默认值是 2000 毫秒（2 秒）。\n如果你希望更快速地检测和分割语音片段，可以减小这个值，比如设置为 500 毫秒；\n如果希望更宽松地分割，可以将其增大' if config.defaulelang == 'zh' else 'Minimum silence duration (ms)')
        self.hfaster_layout.addWidget(self.min_silence_duration_ms_label)
        self.hfaster_layout.addWidget(self.min_silence_duration_ms)

        self.max_speech_duration_s_label = QtWidgets.QLabel()
        self.max_speech_duration_s_label.setText('max_speech_duration_s' if config.defaulelang != 'zh' else '最大语音持续时长')
        self.max_speech_duration_s_label.setVisible(False)
        self.max_speech_duration_s = QtWidgets.QLineEdit()
        self.max_speech_duration_s.setPlaceholderText('200ms')
        self.max_speech_duration_s.setMaximumWidth(80)
        self.max_speech_duration_s.setVisible(False)
        self.max_speech_duration_s.setText(str(config.settings.get('max_speech_duration_s', 2000)))
        self.max_speech_duration_s.setToolTip(
            '最大语音持续时间，单位：秒。\n单个语音片段的最大长度。如果语音片段超过这个时长，则会尝试在 100 毫秒以上的静音处进行分割。\n如果没有找到静音位置，则会在该时长前强行分割，避免过长的连续片段。默认是无穷大（不限制），\n如果需要处理较长的语音片段，可以保留默认值；\n但如果你希望控制片段长度，比如处理对话或分段输出，\n可以根据具体需求设定，比如 10 秒或 30 秒。 0表示无穷大' if config.defaulelang == 'zh' else 'max speech duration (s)')
        self.hfaster_layout.addWidget(self.max_speech_duration_s_label)
        self.hfaster_layout.addWidget(self.max_speech_duration_s)

        self.speech_pad_ms_label = QtWidgets.QLabel()
        self.speech_pad_ms_label.setText('speech_pad_ms' if config.defaulelang != 'zh' else '填充毫秒')
        self.speech_pad_ms_label.setVisible(False)
        self.speech_pad_ms = QtWidgets.QLineEdit()
        self.speech_pad_ms.setPlaceholderText('200ms')
        self.speech_pad_ms.setMaximumWidth(80)
        self.speech_pad_ms.setVisible(False)
        self.speech_pad_ms.setToolTip(
            '语音填充时间，单位：毫秒。\n在检测到的语音片段前后各添加的填充时间，避免语音片段切割得太紧凑，可能会切掉一些边缘的语音。\n默认值是 400 毫秒。如果你发现切割后的语音片段有缺失部分，可以增大该值，比如 500 毫秒或 800 毫秒。\n反之，如果语音片段过长或包含过多的无效部分，可以减少这个值' if config.defaulelang == 'zh' else 'Speech padding (ms)')
        self.speech_pad_ms.setText(str(config.settings.get('speech_pad_ms', 400)))
        self.hfaster_layout.addWidget(self.speech_pad_ms_label)
        self.hfaster_layout.addWidget(self.speech_pad_ms)



        self.verticalLayout_3.addLayout(self.hfaster_layout)
        self.verticalLayout_3.addLayout(h4)


        self.loglabel = QtWidgets.QPushButton()
        self.loglabel.setStyleSheet('''color:#148cd2;background-color:transparent''')
        self.verticalLayout_3.addWidget(self.loglabel)

        self.shibie_text = QtWidgets.QPlainTextEdit()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shibie_text.sizePolicy().hasHeightForWidth())
        self.shibie_text.setSizePolicy(sizePolicy)
        self.shibie_text.setObjectName("shibie_text")
        self.shibie_text.setReadOnly(True)
        self.verticalLayout_3.addWidget(self.shibie_text)



        self.shibie_opendir = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shibie_opendir.sizePolicy().hasHeightForWidth())
        self.shibie_opendir.setSizePolicy(sizePolicy)
        self.shibie_opendir.setFixedHeight(30)
        self.shibie_opendir.setObjectName("shibie_opendir")
        self.shibie_opendir.setText('打开识别结果保存目录' if config.defaulelang == 'zh' else 'Open Output dir')
        self.shibie_opendir.setDisabled(True)
        self.shibie_opendir.setCursor(Qt.PointingHandCursor)

        self.horizontalLayout_shibie8 = QtWidgets.QHBoxLayout()

        self.horizontalLayout_shibie8.addWidget(self.shibie_opendir)
        self.verticalLayout_3.addLayout(self.horizontalLayout_shibie8)

        self.label_shibie10 = QtWidgets.QLabel()
        self.verticalLayout_3.addWidget(self.label_shibie10)

        self.horizontalLayout_9.addLayout(self.verticalLayout_3)

        self.retranslateUi(recogn)
        QtCore.QMetaObject.connectSlotsByName(recogn)

    def retranslateUi(self, recogn):
        recogn.setWindowTitle(config.uilanglist.get("Speech Recognition Text"))
        self.label_3.setText(box_lang.get("Source lang"))
        self.shibie_startbtn.setText(box_lang.get("Start"))
