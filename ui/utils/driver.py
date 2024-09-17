from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Driver:
    @staticmethod
    def get_driver():
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--no-first-run")
        options.add_argument("--disable-features=OptimizationHints,OptimizationHintsFetching,Translate,"
                             "OptimizationTargetPrediction,OptimizationGuideModelDownloading,DownloadBubble,"
                             "DownloadBubbleV2,InsecureDownloadWarnings,InterestFeedContentSuggestions,"
                             "SidePanelPinning")
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
