import yaml
import os
from crawler import crawl
import unittest


class TestCrawler(unittest.TestCase):
    def test_crawler_html(self):
        # this website is a site for webscraper training shouldn't change that much over time
        testcase_string = 'DOCTYPEhtmlhtmllangenheadAntiflickersnippetrecommendedstyleasynchideopacity0importantstylescriptfunctionasynchidesclassNameyhstart1newDatehendifunctionsclassNamesclassNamereplaceRegExpyananhidehsetTimeoutfunctionihendnullchtimeoutcwindowdocumentdocumentElementasynchidedataLayer4000GTMNVFPDWBtruescriptGoogleTagManagerscriptfunctionwdsliwlwlwlpushgtmstartnewDategetTimeeventgtmjsvarfdgetElementsByTagNames0jdcreateElementsdlldataLayerlljasynctruejsrchttpswwwgoogletagmanagercomgtmjsididlfparentNodeinsertBeforejfwindowdocumentscriptdataLayerGTMNVFPDWBscriptEndGoogleTagManagertitleWebScraperTestSitestitlemetacharsetutf8metahttpequivXUACompatiblecontentIEedgechrome1metanamekeywordscontentwebscrapingWebScraperChromeextensionCrawlingCrossplatformscrapermetanamedescriptioncontentThemostpopularwebscrapingextensionStartscrapinginminutesAutomateyourtaskswithourCloudScraperNosoftwaretodownloadnocodingneededlinkreliconsizes128x128hreffaviconpngmetanameviewportcontentwidthdevicewidthinitialscale10linkrelstylesheethrefcssappcsside30a09b05325a08d79ddlinkrelcanonicalhrefhttpswebscraperiotestsitestableslinkrelappletouchiconhrefimglogoiconpngscriptdefersrcjsappjsid1c1cafc4a642f71eb469scriptheadbodyGoogleTagManagernoscriptnoscriptiframesrchttpswwwgoogletagmanagercomnshtmlidGTMNVFPDWBheight0width0styledisplaynonevisibilityhiddeniframenoscriptEndGoogleTagManagernoscriptheaderrolebannerclassnavbarnavbarfixedtopnavbarstaticdivclasscontainerdivclassnavbarheaderadatatogglecollapsesidedatatargetsidecollapsedatatarget2sidecollapsecontainerbuttontypebuttonclassnavbartogglepullrightcollapseddatatogglecollapsedatatargetnavbardatatarget2sidecollapsecontainerdatatarget3sidecollapseariaexpandedfalseariacontrolsnavbarspanclasssronlyTogglenavigationspanspanclassiconbartopbarspanspanclassiconbarmiddlebarspanspanclassiconbarbottombarspanbuttonadivclassnavbarbrandahrefimgsrcimglogowhitesvgaltWebScraperadivdivdivclasssidecollapseinnavidnavbarrolenavigationclassnavbarcollapsecollapseulclassnavnavbarnavnavbarrightliclasshiddenahrefpagetopaliliahrefclassmenuitmpWebScraperpdivclasscrtadivaliliahrefcloudscraperclassmenuitmpCloudScraperpdivclasscrtadivaliliahrefpricingclassmenuitmpPricingpdivclasscrtadivaliliclassdropdownahrefsection3classmenuitmdropdowntoggledatatoggledropdownpLearnpdivclasscrtadivaulclassdropdownmenuliahrefdocumentationDocumentationaliliahreftutorialsVideoTutorialsaliliahrefhowtovideosHowtoaliliahreftestsitesTestSitesaliliahrefhttpsforumwebscraperiotargetblankrelnoopenerForumaliulliliatargetblankhrefhttpschromegooglecomwebstoredetailwebscraperjnhgnonknehpejjnehehllkliplmbmhnhlenclassbtnmenu1installextensionrelnoopenerInstallaliliahrefhttpscloudwebscraperioclassbtnmenu2Loginaliulnavdivdivheaderdivclasswrapperdivclassformenuherecontainerfluiddivdivclasscontainerfluidblogherodivclasscontainerdivclassrowdivclasscolmd12h1Tableplaygroundh1divdivdivdivdivclasscontainerpYoucantrainusingTableselectorherephrh2Semanticallycorrecttablewiththeadandtbodyh2pTableselectorautomaticallydetectsheaderanddatarowsptableclasstabletableborderedtheadtrthththFirstNameththLastNameththUsernamethtrtheadtbodytrtd1tdtdMarktdtdOttotdtdmdotdtrtrtd2tdtdJacobtdtdThorntontdtdfattdtrtrtd3tdtdLarrytdtdtheBirdtdtdtwittertdtrtbodytabletableclasstabletableborderedtheadtrthththFirstNameththLastNameththUsernamethtrtheadtbodytrtd4tdtdHarrytdtdPottertdtdhptdtrtrtd5tdtdJohntdtdSnowtdtddunnotdtrtrtd6tdtdTimtdtdBeantdtdtimbeantdtrtbodytablehrh2Tablewithouttheadtagh2pTableselectorautomaticallydetectsheaderanddatarowsptableclasstabletableborderedtbodytrthththFirstNameththLastNameththUsernamethtrtrtd1tdtdMarktdtdOttotdtdmdotdtrtrtd2tdtdJacobtdtdThorntontdtdfattdtrtrtd3tdtdLarrytdtdtheBirdtdtdtwittertdtrtbodytableh2Tablewithmultipleheaderrowsandanemptydatarowh2pYoumustmanuallyselectheaderanddatarowsptableclasstabletableborderedtbodytrthththcolspan2PersonththUserdatathtrtrthththFirstNameththLastNameththUsernamethtrtrtdtdtdtdtdtdtdtdtrtrtd1tdtdMarktdtdOttotdtdmdotdtrtrtd2tdtdJacobtdtdThorntontdtdfattdtrtrtd3tdtdLarrytdtdtheBirdtdtdtwittertdtrtbodytabledivdivclassclearfixdivdivclasspushdivdivdivclasscontainerfluidfooteridlayoutfooterdivclasscontainerdivclassrowdivclasscolmd3ullipProductspliliahrefWebScraperbrowserextensionaliliahrefpricingWebScraperCloudaliuldivdivclasscolmd3ullipCompanypliliahrefcontactContactaliliahrefprivacypolicyWebsitePrivacyPolicyaliliahrefextensionprivacypolicyBrowserExtensionPrivacyPolicyaliliahrefhttpwebscraperiouseast1elasticbeanstalkcomdownloadsWebScraperMediaKitzipMediakitaliliahrefjobsJobsaliuldivdivclasscolmd3ullipResourcespliliahrefblogBlogaliliahrefdocumentationDocumentationaliliahreftutorialsVideoTutorialsaliliahrefscreenshotsScreenshotsaliliahreftestsitesTestSitesaliliatargetblankhrefhttpsforumwebscraperiorelnoopenerForumaliuldivdivclasscolmd3ullipCONTACTUSpliliahrefmailtoinfowebscraperioinfowebscraperioaliliRupniecibasiela30brRigaLatviaLV1045liululclasssmedialiahrefhttpswwwfacebookcomwebscraperiotargetblankrelnoopenerimgsrcimgfbiconpngaltWebScraperonFacebookaliliahrefhttpstwittercomwebscraperiotargetblankrelnoopenerimgsrcimgtwiconpngaltWebScraperonTwitteraliuldivdivdivclassrowdivclasscolmd12pclasscopyrightCopyrightcopy2022ahrefWebScraperaAllrightsreservedMadebyzoom59pdivdivdivdivbodyhtml'

        url = ["https://webscraper.io/test-sites/tables"]
        settings = {"client": "linux",
                    "logconfig": {
                        "version": 1,
                        "root": {
                            "handlers": [
                                "console_handler",
                                "file_handler"
                            ],
                            "propagate": True,
                            "level": "DEBUG"
                        },
                        "formatters": {
                            "simple": {
                                "format": "%(asctime)s %(levelname)s:%(message)s"
                            },
                            "standard": {
                                "datefmt": "%m/%d/%Y|%I:%M:%S|%p",
                                "format": " %(asctime)s: (%(filename)s): %(levelname)s: %(funcName)s Line: %(lineno)d - %(message)s"
                            }
                        },
                        "disable_existing_loggers": True,
                        "handlers": {
                            "console_handler": {
                                "formatter": "simple",
                                "class": "logging.StreamHandler",
                                "level": "WARNING"
                            },
                            "file_handler": {
                                "class": "logging.FileHandler",
                                "formatter": "standard",
                                "mode": "a",
                                "level": "DEBUG",
                                "filename": "logging/logging.logging"
                            }
                        }
                    }
                    }

        url_file = open("testURL.yaml", "w")
        yaml.dump(url, url_file)
        url_file.close()

        settings_file = open("testsettings.yaml", "w")
        yaml.dump(settings, settings_file)
        settings_file.close()

        # start of the actual test

        html_response = crawl("testURL.yaml", "testsettings.yaml")
        html_response = "".join(char for char in html_response if char.isalnum())
        os.remove("testsettings.yaml")
        os.remove("testURL.yaml")

        # the testcase_string variable is initialized at the start of this method
        self.assertEqual(html_response, testcase_string, "The test string and the data scraped by the crawler do not match.")
