/**********************************************************
 *            AUTOGENERATED FILE                          *
 *             DO NOT MODIFY IT                           *
 *                                                        *
 * To add new commands :                                  *
 *  - Modify ../Xml/commands.xml file                     *
 *  - Re-run generateDeviceControllers.py script          *
 *                                                        *
 **********************************************************/

/**
 * @file ARFeatureWifi.java
 * @brief Feature controller allow to send command related of wifi Feature.
 * All commands/events related to the Wifi
 */
package com.parrot.arsdk.arcontroller;

import com.parrot.arsdk.arsal.ARSALPrint;
import com.parrot.arsdk.arcommands.*;
import com.parrot.arsdk.ardiscovery.ARDiscoveryDevice;

import java.util.List;
import java.util.ArrayList;

public class ARFeatureWifi
{
    private static String TAG = "ARFeatureWifi";
    
    public static String ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_SSID = ""; /**< Key of the argument </code>ssid</code> of event <code>ScannedItem</code> in feature <code>Wifi</code> */
    public static String ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_RSSI = ""; /**< Key of the argument </code>rssi</code> of event <code>ScannedItem</code> in feature <code>Wifi</code> */
    public static String ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_BAND = ""; /**< Key of the argument </code>band</code> of event <code>ScannedItem</code> in feature <code>Wifi</code> */
    public static String ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_CHANNEL = ""; /**< Key of the argument </code>channel</code> of event <code>ScannedItem</code> in feature <code>Wifi</code> */
    public static String ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_LIST_FLAGS = ""; /**< Key of the argument </code>list_flags</code> of event <code>ScannedItem</code> in feature <code>Wifi</code> */
    public static String ARCONTROLLER_DICTIONARY_KEY_WIFI_AUTHORIZEDCHANNEL_BAND = ""; /**< Key of the argument </code>band</code> of event <code>AuthorizedChannel</code> in feature <code>Wifi</code> */
    public static String ARCONTROLLER_DICTIONARY_KEY_WIFI_AUTHORIZEDCHANNEL_CHANNEL = ""; /**< Key of the argument </code>channel</code> of event <code>AuthorizedChannel</code> in feature <code>Wifi</code> */
    public static String ARCONTROLLER_DICTIONARY_KEY_WIFI_AUTHORIZEDCHANNEL_ENVIRONEMENT = ""; /**< Key of the argument </code>environement</code> of event <code>AuthorizedChannel</code> in feature <code>Wifi</code> */
    public static String ARCONTROLLER_DICTIONARY_KEY_WIFI_AUTHORIZEDCHANNEL_LIST_FLAGS = ""; /**< Key of the argument </code>list_flags</code> of event <code>AuthorizedChannel</code> in feature <code>Wifi</code> */
    public static String ARCONTROLLER_DICTIONARY_KEY_WIFI_APCHANNELCHANGED_TYPE = ""; /**< Key of the argument </code>type</code> of event <code>ApChannelChanged</code> in feature <code>Wifi</code> */
    public static String ARCONTROLLER_DICTIONARY_KEY_WIFI_APCHANNELCHANGED_BAND = ""; /**< Key of the argument </code>band</code> of event <code>ApChannelChanged</code> in feature <code>Wifi</code> */
    public static String ARCONTROLLER_DICTIONARY_KEY_WIFI_APCHANNELCHANGED_CHANNEL = ""; /**< Key of the argument </code>channel</code> of event <code>ApChannelChanged</code> in feature <code>Wifi</code> */
    public static String ARCONTROLLER_DICTIONARY_KEY_WIFI_SECURITYCHANGED_KEY = ""; /**< Key of the argument </code>key</code> of event <code>SecurityChanged</code> in feature <code>Wifi</code> */
    public static String ARCONTROLLER_DICTIONARY_KEY_WIFI_SECURITYCHANGED_KEY_TYPE = ""; /**< Key of the argument </code>key_type</code> of event <code>SecurityChanged</code> in feature <code>Wifi</code> */
    public static String ARCONTROLLER_DICTIONARY_KEY_WIFI_COUNTRYCHANGED_SELECTION_MODE = ""; /**< Key of the argument </code>selection_mode</code> of event <code>CountryChanged</code> in feature <code>Wifi</code> */
    public static String ARCONTROLLER_DICTIONARY_KEY_WIFI_COUNTRYCHANGED_CODE = ""; /**< Key of the argument </code>code</code> of event <code>CountryChanged</code> in feature <code>Wifi</code> */
    public static String ARCONTROLLER_DICTIONARY_KEY_WIFI_ENVIRONEMENTCHANGED_ENVIRONEMENT = ""; /**< Key of the argument </code>environement</code> of event <code>EnvironementChanged</code> in feature <code>Wifi</code> */
    public static String ARCONTROLLER_DICTIONARY_KEY_WIFI_RSSICHANGED_RSSI = ""; /**< Key of the argument </code>rssi</code> of event <code>RssiChanged</code> in feature <code>Wifi</code> */

    private static native String nativeStaticGetKeyWifiScannedItemSsid ();
    private static native String nativeStaticGetKeyWifiScannedItemRssi ();
    private static native String nativeStaticGetKeyWifiScannedItemBand ();
    private static native String nativeStaticGetKeyWifiScannedItemChannel ();
    private static native String nativeStaticGetKeyWifiScannedItemListflags ();
    private static native String nativeStaticGetKeyWifiAuthorizedChannelBand ();
    private static native String nativeStaticGetKeyWifiAuthorizedChannelChannel ();
    private static native String nativeStaticGetKeyWifiAuthorizedChannelEnvironement ();
    private static native String nativeStaticGetKeyWifiAuthorizedChannelListflags ();
    private static native String nativeStaticGetKeyWifiApChannelChangedType ();
    private static native String nativeStaticGetKeyWifiApChannelChangedBand ();
    private static native String nativeStaticGetKeyWifiApChannelChangedChannel ();
    private static native String nativeStaticGetKeyWifiSecurityChangedKey ();
    private static native String nativeStaticGetKeyWifiSecurityChangedKeytype ();
    private static native String nativeStaticGetKeyWifiCountryChangedSelectionmode ();
    private static native String nativeStaticGetKeyWifiCountryChangedCode ();
    private static native String nativeStaticGetKeyWifiEnvironementChangedEnvironement ();
    private static native String nativeStaticGetKeyWifiRssiChangedRssi ();

    private native int nativeSendScan (long jFeature, byte band);
    private native int nativeSendUpdateAuthorizedChannels (long jFeature);
    private native int nativeSendSetApChannel (long jFeature, int type, int band, byte channel);
    private native int nativeSendSetSecurity (long jFeature, int type, String key, int key_type);
    private native int nativeSendSetCountry (long jFeature, int selection_mode, String code);
    private native int nativeSendSetEnvironement (long jFeature, int environement);

    private long jniFeature;
    private boolean initOk;
    
    static
    {
        ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_SSID = nativeStaticGetKeyWifiScannedItemSsid ();
        ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_RSSI = nativeStaticGetKeyWifiScannedItemRssi ();
        ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_BAND = nativeStaticGetKeyWifiScannedItemBand ();
        ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_CHANNEL = nativeStaticGetKeyWifiScannedItemChannel ();
        ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_LIST_FLAGS = nativeStaticGetKeyWifiScannedItemListflags ();
        ARCONTROLLER_DICTIONARY_KEY_WIFI_AUTHORIZEDCHANNEL_BAND = nativeStaticGetKeyWifiAuthorizedChannelBand ();
        ARCONTROLLER_DICTIONARY_KEY_WIFI_AUTHORIZEDCHANNEL_CHANNEL = nativeStaticGetKeyWifiAuthorizedChannelChannel ();
        ARCONTROLLER_DICTIONARY_KEY_WIFI_AUTHORIZEDCHANNEL_ENVIRONEMENT = nativeStaticGetKeyWifiAuthorizedChannelEnvironement ();
        ARCONTROLLER_DICTIONARY_KEY_WIFI_AUTHORIZEDCHANNEL_LIST_FLAGS = nativeStaticGetKeyWifiAuthorizedChannelListflags ();
        ARCONTROLLER_DICTIONARY_KEY_WIFI_APCHANNELCHANGED_TYPE = nativeStaticGetKeyWifiApChannelChangedType ();
        ARCONTROLLER_DICTIONARY_KEY_WIFI_APCHANNELCHANGED_BAND = nativeStaticGetKeyWifiApChannelChangedBand ();
        ARCONTROLLER_DICTIONARY_KEY_WIFI_APCHANNELCHANGED_CHANNEL = nativeStaticGetKeyWifiApChannelChangedChannel ();
        ARCONTROLLER_DICTIONARY_KEY_WIFI_SECURITYCHANGED_KEY = nativeStaticGetKeyWifiSecurityChangedKey ();
        ARCONTROLLER_DICTIONARY_KEY_WIFI_SECURITYCHANGED_KEY_TYPE = nativeStaticGetKeyWifiSecurityChangedKeytype ();
        ARCONTROLLER_DICTIONARY_KEY_WIFI_COUNTRYCHANGED_SELECTION_MODE = nativeStaticGetKeyWifiCountryChangedSelectionmode ();
        ARCONTROLLER_DICTIONARY_KEY_WIFI_COUNTRYCHANGED_CODE = nativeStaticGetKeyWifiCountryChangedCode ();
        ARCONTROLLER_DICTIONARY_KEY_WIFI_ENVIRONEMENTCHANGED_ENVIRONEMENT = nativeStaticGetKeyWifiEnvironementChangedEnvironement ();
        ARCONTROLLER_DICTIONARY_KEY_WIFI_RSSICHANGED_RSSI = nativeStaticGetKeyWifiRssiChangedRssi ();
    }
    
    /**
     * Constructor
     */
    public ARFeatureWifi (long nativeFeature)
    {
        initOk = false;
        
        if (nativeFeature != 0)
        {
            jniFeature = nativeFeature;
            initOk = true;
        }
    }

    /**
     * Dispose
     */
    public void dispose()
    {
        ARCONTROLLER_ERROR_ENUM error = ARCONTROLLER_ERROR_ENUM.ARCONTROLLER_OK;
        synchronized (this)
        {
            if(initOk == true)
            {
                jniFeature = 0;
                initOk = false;
            }
        }
    }

    /**
     * Destructor
     */
    public void finalize () throws Throwable
    {
        try
        {
            dispose ();
        }
        finally
        {
            super.finalize ();
        }
    }
    
    public ARCONTROLLER_ERROR_ENUM sendScan (byte _band)
    {
        ARCONTROLLER_ERROR_ENUM error = ARCONTROLLER_ERROR_ENUM.ARCONTROLLER_OK;
        synchronized (this)
        {
            if(initOk == true)
            {
                int nativeError = nativeSendScan (jniFeature, _band);
                error = ARCONTROLLER_ERROR_ENUM.getFromValue(nativeError);
            }
        }
        return error;
    }
    
    public ARCONTROLLER_ERROR_ENUM sendUpdateAuthorizedChannels ()
    {
        ARCONTROLLER_ERROR_ENUM error = ARCONTROLLER_ERROR_ENUM.ARCONTROLLER_OK;
        synchronized (this)
        {
            if(initOk == true)
            {
                int nativeError = nativeSendUpdateAuthorizedChannels (jniFeature);
                error = ARCONTROLLER_ERROR_ENUM.getFromValue(nativeError);
            }
        }
        return error;
    }
    
    public ARCONTROLLER_ERROR_ENUM sendSetApChannel (ARCOMMANDS_WIFI_SELECTION_TYPE_ENUM _type, ARCOMMANDS_WIFI_BAND_ENUM _band, byte _channel)
    {
        ARCONTROLLER_ERROR_ENUM error = ARCONTROLLER_ERROR_ENUM.ARCONTROLLER_OK;
        synchronized (this)
        {
            if(initOk == true)
            {
                int nativeError = nativeSendSetApChannel (jniFeature, _type.getValue(), _band.getValue(), _channel);
                error = ARCONTROLLER_ERROR_ENUM.getFromValue(nativeError);
            }
        }
        return error;
    }
    
    public ARCONTROLLER_ERROR_ENUM sendSetSecurity (ARCOMMANDS_WIFI_SECURITY_TYPE_ENUM _type, String _key, ARCOMMANDS_WIFI_SECURITY_KEY_TYPE_ENUM _key_type)
    {
        ARCONTROLLER_ERROR_ENUM error = ARCONTROLLER_ERROR_ENUM.ARCONTROLLER_OK;
        synchronized (this)
        {
            if(initOk == true)
            {
                int nativeError = nativeSendSetSecurity (jniFeature, _type.getValue(), _key, _key_type.getValue());
                error = ARCONTROLLER_ERROR_ENUM.getFromValue(nativeError);
            }
        }
        return error;
    }
    
    public ARCONTROLLER_ERROR_ENUM sendSetCountry (ARCOMMANDS_WIFI_COUNTRY_SELECTION_ENUM _selection_mode, String _code)
    {
        ARCONTROLLER_ERROR_ENUM error = ARCONTROLLER_ERROR_ENUM.ARCONTROLLER_OK;
        synchronized (this)
        {
            if(initOk == true)
            {
                int nativeError = nativeSendSetCountry (jniFeature, _selection_mode.getValue(), _code);
                error = ARCONTROLLER_ERROR_ENUM.getFromValue(nativeError);
            }
        }
        return error;
    }
    
    public ARCONTROLLER_ERROR_ENUM sendSetEnvironement (ARCOMMANDS_WIFI_ENVIRONEMENT_ENUM _environement)
    {
        ARCONTROLLER_ERROR_ENUM error = ARCONTROLLER_ERROR_ENUM.ARCONTROLLER_OK;
        synchronized (this)
        {
            if(initOk == true)
            {
                int nativeError = nativeSendSetEnvironement (jniFeature, _environement.getValue());
                error = ARCONTROLLER_ERROR_ENUM.getFromValue(nativeError);
            }
        }
        return error;
    }
    

}

