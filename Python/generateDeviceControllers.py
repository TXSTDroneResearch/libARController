#!/usr/bin/env python

'''
    Copyright (C) 2014 Parrot SA

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions
    are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in
      the documentation and/or other materials provided with the 
      distribution.
    * Neither the name of Parrot nor the names
      of its contributors may be used to endorse or promote products
      derived from this software without specific prior written
      permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
    FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
    COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
    INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
    BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
    OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED 
    AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
    OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
    SUCH DAMAGE.
'''

import sys
import os
import re

MYDIR=os.path.abspath(os.path.dirname(sys.argv[0]))
if '' == MYDIR:
    MYDIR=os.getcwd()

sys.path.append('%(MYDIR)s/../../ARBuildUtils/Utils/Python' % locals())

DEVICE_CONTROLLER_FILE_NAME = 'deviceControllers.xml'
DEVICE_CONTROLLER_FILE = MYDIR+'/../Xml/'+DEVICE_CONTROLLER_FILE_NAME

from ARFuncs import *
from ARCommandsParser import *
from ARControllerUtils import *

def generateDeviceControllers (allFeatures, SRC_DIR, INC_DIR):
    
    deviceControllers = parseDeviceControllersXml (DEVICE_CONTROLLER_FILE, allFeatures)
    
    #check deviceController list
    if not deviceControllers:
        exit (1)
        
    ARPrint ('deviceControllers ...')
    for d in deviceControllers:
        ARPrint ('    name: ' + d.name)
    
    ARPrint ('generateDeviceControllers ...')
    
    #########################################
    # Write Feature controller header file  #
    #########################################

    includeDefine = '_' + MODULE_DEVICE + '_H_'
    bref='Device controller allow to drive a device.'
    className = ARTypeName (MODULE_ARCONTROLLER, 'device', '')
    classPrivateName = ARTypeName (MODULE_ARCONTROLLER, 'device', 'private')

    headerFileName = 'ARCONTROLLER_Device.h'
    filepath = INC_DIR + headerFileName
    hfile = open (filepath, 'w')

    hfile.write ('/**********************************************************\n')
    hfile.write (' *            AUTOGENERATED FILE                          *\n')
    hfile.write (' *             DO NOT MODIFY IT                           *\n')
    hfile.write (' *                                                        *\n')
    hfile.write (' * To add new commands :                                  *\n')
    hfile.write (' *  - Modify ../Xml/commands.xml file                     *\n')
    hfile.write (' *  - Re-run generateDeviceControllers.py script          *\n')
    hfile.write (' *                                                        *\n')
    hfile.write (' **********************************************************/\n')
    hfile.write ('\n')

    hfile.write ('/**\n')
    hfile.write ('* @file '+headerFileName+'\n')
    hfile.write ('* @brief '+bref+'\n')
    hfile.write ('*/\n')
    hfile.write ('\n')

    hfile.write ('#ifndef '+includeDefine+'\n')
    hfile.write ('#define '+includeDefine+'\n')
    hfile.write ('\n')

    hfile.write ('#include <stdlib.h>\n')
    hfile.write ('\n')
    hfile.write ('#include <libARSAL/ARSAL_Print.h>\n')
    hfile.write ('#include <libARSAL/ARSAL_Mutex.h>\n')
    hfile.write ('#include <libuthash/uthash.h>\n')
    hfile.write ('\n')
    hfile.write ('#include <libARController/ARCONTROLLER_Error.h>\n')
    hfile.write ('#include <libARController/ARCONTROLLER_Command.h>\n')
    hfile.write ('#include <libARController/ARCONTROLLER_Feature.h>\n')
    hfile.write ('\n')
    
    hfile.write ('/**\n')
    hfile.write (' * Enum characterizing the states of the device controller\n')
    hfile.write (' */\n')
    hfile.write ('typedef enum\n')
    hfile.write ('{\n')
    hfile.write ('    ARCONTROLLER_DEVICE_STATE_STOPPED = 0, /**< device controller stopped */\n')
    hfile.write ('    ARCONTROLLER_DEVICE_STATE_RUNNING, /**< device controller running */\n')
    hfile.write ('    ARCONTROLLER_DEVICE_STATE_PAUSE, /**< device controller in pause */\n')
    hfile.write ('    \n')
    hfile.write ('    ARCONTROLLER_DEVICE_STATE_MAX /**< Max of the enumeration */\n')
    hfile.write ('}\n')
    hfile.write ('eARCONTROLLER_DEVICE_STATE;\n')
    hfile.write ('\n')
    
    hfile.write ('/**\n')
    hfile.write (' * @brief private part of the Device controller.\n')
    hfile.write (' */\n')
    hfile.write ('typedef struct '+classPrivateName+' '+classPrivateName+';\n')
    hfile.write ('\n')

    hfile.write ('/**\n')
    hfile.write (' * @brief Device controller allow to drive a device.\n')
    hfile.write (' */\n')
    hfile.write ('typedef struct\n')
    hfile.write ('{\n')
    for feature in allFeatures:
        hfile.write ('    '+ARTypeName (MODULE_FEATURE, feature.name, '')+' *'+ARUncapitalize(feature.name)+'; /**< */\n') # TODO add Commentary !!!!!!!!!!
    hfile.write ('    '+classPrivateName+' *privatePart; /**< private part of the deviceController */\n')
    hfile.write ('}'+className+';\n')
    hfile.write ('\n')
    
    hfile.write ('/**\n')
    hfile.write (' * @brief Create a new Device Controller\n')
    hfile.write (' * @warning This function allocate memory\n')
    hfile.write (' * @post ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'Delete')+'() must be called to delete the Device Controller and free the memory allocated.\n')
    hfile.write (' * @param[in] discoveryDevice The device to drive ; must be not NULL.\n')
    hfile.write (' * @param[out] error executing error.\n')
    hfile.write (' * @return the new Device Controller\n')
    hfile.write (' * @see ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'Delete')+'\n')
    hfile.write (' */\n')
    hfile.write (''+className+' *' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'New')+' (ARDISCOVERY_Device_t *discoveryDevice, eARCONTROLLER_ERROR *error);\n')
    hfile.write ('\n')
    
    hfile.write ('/**\n')
    hfile.write (' * @brief Delete the Device Controller\n')
    hfile.write (' * @warning This function free memory\n')
    hfile.write (' * @param device The device controller to delete\n')
    hfile.write (' * @see ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'New')+'\n')
    hfile.write (' */\n')
    hfile.write ('void ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'Delete')+' ('+className+' **deviceController);\n')
    hfile.write ('\n')
    
    
    hfile.write ('#endif /* '+includeDefine+' */\n')
    hfile.write ('\n')
    hfile.write ('// END GENERATED CODE\n')
    hfile.close ()
    
    #################################################
    # Write Feature controller private header file  #
    #################################################

    includeDefine = '_' + MODULE_DEVICE + '_PRIVATE_H_'

    headerPrivateFileName = 'ARCONTROLLER_Device' + '.h'
    filepath = SRC_DIR + headerPrivateFileName
    hPrivFile = open (filepath, 'w')

    hPrivFile.write ('/**********************************************************\n')
    hPrivFile.write (' *            AUTOGENERATED FILE                          *\n')
    hPrivFile.write (' *             DO NOT MODIFY IT                           *\n')
    hPrivFile.write (' *                                                        *\n')
    hPrivFile.write (' * To add new commands :                                  *\n')
    hPrivFile.write (' *  - Modify ../Xml/commands.xml file                     *\n')
    hPrivFile.write (' *  - Re-run generateDeviceControllers.py script          *\n')
    hPrivFile.write (' *                                                        *\n')
    hPrivFile.write (' **********************************************************/\n')
    hPrivFile.write ('\n')

    hPrivFile.write ('/**\n')
    hPrivFile.write ('* @file '+headerPrivateFileName+'\n')
    hPrivFile.write ('* @brief '+bref+'\n')
    hPrivFile.write ('*/\n')
    hPrivFile.write ('\n')

    hPrivFile.write ('#ifndef '+includeDefine+'\n')
    hPrivFile.write ('#define '+includeDefine+'\n')
    hPrivFile.write ('\n')
    hPrivFile.write ('#include <libARSAL/ARSAL_Mutex.h>\n')
    hPrivFile.write ('#include <libARCommands/ARCommands.h>\n')
    hPrivFile.write ('#include <libARController/ARCONTROLLER_Feature.h>\n')
    hPrivFile.write ('\n')
    
    hPrivFile.write ('/**\n')
    hPrivFile.write (' * @brief Device controller allow to drive a device.\n')
    hPrivFile.write (' */\n')
    hPrivFile.write ('struct '+classPrivateName+'\n')
    hPrivFile.write ('{\n')
    hPrivFile.write ('    ARDISCOVERY_Device_t *discoveryDevice; /**< the device to drive */\n')
    hPrivFile.write ('    ARCONTROLLER_Network_t *networkController; /**< Mutex for multithreading */\n')
    hPrivFile.write ('    ARSAL_Mutex_t mutex; /**< Mutex for multithreading */\n')
    hPrivFile.write ('    eARCONTROLLER_DEVICE_STATE state; /**< state of the deviceController*/\n')
    hPrivFile.write ('};\n')
    hPrivFile.write ('\n')
    
    #TODO add commentary !!!!!!!!
    hPrivFile.write ('eARCONTROLLER_ERROR ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'RegisterCallbacks')+' ('+className+' *deviceController);\n')
    hPrivFile.write ('\n')
    
    #TODO add commentary !!!!!!!!
    hPrivFile.write ('eARCONTROLLER_ERROR ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'UnregisterCallbacks')+' ('+className+' *deviceController);\n')
    hPrivFile.write ('\n')
    
    #TODO add commentary !!!!!!!!
    hPrivFile.write ('//eARCONTROLLER_ERROR ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'SetInitialDate')+' ('+className+' *deviceController);\n')
    hPrivFile.write ('\n')
    
    #TODO add commentary !!!!!!!!
    hPrivFile.write ('//eARCONTROLLER_ERROR ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'GetInitialSettings')+' ('+className+' *deviceController);\n')
    hPrivFile.write ('\n')
    
    #TODO add commentary !!!!!!!!
    hPrivFile.write ('eARCONTROLLER_ERROR ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'GetInitialStates')+' ('+className+' *deviceController);\n')
    hPrivFile.write ('\n')
    
    #TODO add commentary !!!!!!!!
    hPrivFile.write ('void ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'DictionaryChangedCallback')+' (int commandKey, ARCONTROLLER_FEATURE_DICTIONARY_ARG_t *argumentDictionary, void *customData); // TODO int -> ARCommands Big \n')
    hPrivFile.write ('\n')
    
    hPrivFile.write ('#endif /* '+includeDefine+' */\n')
    hPrivFile.write ('\n')
    hPrivFile.write ('// END GENERATED CODE\n')
    hPrivFile.close ()
    
    #################################################
    # Write Feature controller c file               #
    #################################################
    
    classTag = 'ARCONTROLLER_Device'
    className = 'ARCONTROLLER_Device_t'
    
    cFileName = 'ARCONTROLLER_Device.c'
    filepath = SRC_DIR + cFileName
    cFile = open (filepath, 'w')

    cFile.write ('/**********************************************************\n')
    cFile.write (' *            AUTOGENERATED FILE                          *\n')
    cFile.write (' *             DO NOT MODIFY IT                           *\n')
    cFile.write (' *                                                        *\n')
    cFile.write (' * To add new commands :                                  *\n')
    cFile.write (' *  - Modify ../Xml/commands.xml file                     *\n')
    cFile.write (' *  - Re-run generateDeviceControllers.py script          *\n')
    cFile.write (' *                                                        *\n')
    cFile.write (' **********************************************************/\n')
    cFile.write ('\n')

    cFile.write ('/**\n')
    cFile.write ('* @file '+cFileName+'\n')
    cFile.write ('* @brief '+bref+'\n')
    cFile.write ('*/\n')
    cFile.write ('\n')

    cFile.write ('#include <stdio.h>\n')

    cFile.write ('#include <libARSAL/ARSAL_Mutex.h>\n')
    cFile.write ('#include <libARController/ARCONTROLLER_Network.h>\n')
    cFile.write ('#include <libARController/ARCONTROLLER_Feature.h>\n')
    cFile.write ('#include <libARController/ARCONTROLLER_Command.h>\n')
    cFile.write ('#include <libARController/ARCONTROLLER_Device.h>\n')
    cFile.write ('\n')
    cFile.write ('#include "ARCONTROLLER_Device.h"\n')
    cFile.write ('\n')
    cFile.write ('#define '+MODULE_DEVICE+'_TAG "'+classTag+'"\n')
    cFile.write ('\n')
    
    cFile.write (''+className+' *' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'New')+' (ARDISCOVERY_Device_t *discoveryDevice, eARCONTROLLER_ERROR *error)\n')
    cFile.write ('{\n')
    cFile.write ('    // -- Create a new Device Controller --\n')
    cFile.write ('    \n')
    
    cFile.write ('    //local declarations\n')
    cFile.write ('    eARCONTROLLER_ERROR localError = ARCONTROLLER_OK;\n')
    cFile.write ('    '+className+' *deviceController =  NULL;\n')
    cFile.write ('    \n')
    
    cFile.write ('    // check parameters\n')
    cFile.write ('    if (discoveryDevice == NULL)\n')
    cFile.write ('    {\n')
    cFile.write ('        localError = ARCONTROLLER_ERROR_BAD_PARAMETER;\n')
    cFile.write ('    }\n')
    cFile.write ('    // No Else: the checking parameters sets localError to ARNETWORK_ERROR_BAD_PARAMETER and stop the processing\n')
    cFile.write ('    \n')
    
    cFile.write ('    // Allocate the Device Controller\n')
    cFile.write ('    deviceController = malloc (sizeof('+className+'));\n')
    cFile.write ('    if (deviceController != NULL)\n')
    cFile.write ('    {\n')
    cFile.write ('        //initialization of the device controller\n')
    for feature in allFeatures:
        cFile.write ('        deviceController->'+ARUncapitalize(feature.name)+' = NULL;\n')
    cFile.write ('        deviceController->privatePart = NULL;\n')
    cFile.write ('    }\n')
    cFile.write ('    else\n')
    cFile.write ('    {\n')
    cFile.write ('        localError = ARCONTROLLER_ERROR_ALLOC;\n')
    cFile.write ('    }\n')
    cFile.write ('    \n')
    
    cFile.write ('    if (localError == ARCONTROLLER_OK)\n')
    cFile.write ('    {\n')
    cFile.write ('        // Allocate the private part of the Device Controller\n')
    cFile.write ('        deviceController->privatePart = malloc (sizeof('+classPrivateName+'));\n')
    cFile.write ('        if (deviceController != NULL)\n')
    cFile.write ('        {\n')
    cFile.write ('            //initialization of the private part of the device controller\n')
    cFile.write ('            deviceController->privatePart->networkController = NULL;\n')
    cFile.write ('            deviceController->privatePart->state = ARCONTROLLER_DEVICE_STATE_RUNNING;\n')
    cFile.write ('            \n')
    cFile.write ('            /* Create the mutex/condition */\n')
    cFile.write ('            if (ARSAL_Mutex_Init (&(deviceController->privatePart->mutex)) != 0)\n')
    cFile.write ('            {\n')
    cFile.write ('                localError = ARCONTROLLER_ERROR_INIT_MUTEX;\n')
    cFile.write ('            }\n')
    cFile.write ('        }\n')
    cFile.write ('        else\n')
    cFile.write ('        {\n')
    cFile.write ('            localError = ARCONTROLLER_ERROR_ALLOC;\n')
    cFile.write ('        }\n')
    cFile.write ('        \n')
    cFile.write ('    }\n')
    cFile.write ('    // No else: skipped by an error \n')
    cFile.write ('    \n')
    
    cFile.write ('    if (localError == ARCONTROLLER_OK)\n')
    cFile.write ('    {\n')
    cFile.write ('        // Copy the device\n')
    cFile.write ('        eARDISCOVERY_ERROR dicoveryError = ARDISCOVERY_OK;\n')
    cFile.write ('        \n')
    cFile.write ('        deviceController->privatePart->discoveryDevice = ARDISCOVERY_Device_NewByCopy (discoveryDevice, &dicoveryError);\n')
    cFile.write ('        if (dicoveryError != ARDISCOVERY_OK)\n')
    cFile.write ('        {\n')
    cFile.write ('            localError = ARCONTROLLER_ERROR_INIT_DEVICE_COPY;\n')
    cFile.write ('        }\n')
    cFile.write ('    }\n')
    cFile.write ('    \n')
    
    cFile.write ('    if (localError == ARCONTROLLER_OK)\n')
    cFile.write ('    {\n')
    cFile.write ('        // Create the Network Controller\n')
    cFile.write ('        deviceController->privatePart->networkController = ' + ARFunctionName (MODULE_ARCONTROLLER, "Network", 'New') + ' (discoveryDevice, &localError);\n')
    cFile.write ('    }\n')
    cFile.write ('    // No else: skipped by an error\n')
    cFile.write ('    \n')
    
    cFile.write ('    if (localError == ARCONTROLLER_OK)\n')
    cFile.write ('    {\n')
    cFile.write ('        // Creation of the features:\n')
    cFile.write ('        switch (discoveryDevice->productID)\n')
    cFile.write ('        {\n')
    for deviceController in deviceControllers:
        cFile.write ('            case '+discoveryProduct (deviceController.product)+':\n')
        for featureName in deviceController.features:
            cFile.write ('                if (localError == ARCONTROLLER_OK)\n')
            cFile.write ('                {\n')
            cFile.write ('                    deviceController->'+ARUncapitalize(featureName)+' = ' + ARFunctionName (MODULE_FEATURE, featureName, 'New')+' (deviceController->privatePart->networkController, &localError);\n')
            cFile.write ('                }\n')
            cFile.write ('                \n')
        cFile.write ('                break;\n')
        cFile.write ('            \n')
        
    cFile.write ('            default:\n')
    cFile.write ('                ARSAL_PRINT(ARSAL_PRINT_ERROR, '+MODULE_DEVICE+'_TAG, "device : %d not known", discoveryDevice->productID);\n')
    cFile.write ('                break;\n')
    cFile.write ('        }\n')
    cFile.write ('    }\n')
    cFile.write ('    // No else: skipped by an error\n')
    cFile.write ('    \n')
    
    cFile.write ('    if (localError == ARCONTROLLER_OK)\n')
    cFile.write ('    {\n')
    cFile.write ('        localError = ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'Start')+' (deviceController);\n')
    cFile.write ('    }\n')
    cFile.write ('    // No else: skipped by an error\n')
    cFile.write ('    \n')
    
    cFile.write ('    // delete the Device Controller if an error occurred\n')
    cFile.write ('    if (localError != ARCONTROLLER_OK)\n')
    cFile.write ('    {\n')
    cFile.write ('        ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'Delete')+' (&deviceController);\n')
    cFile.write ('    }\n')
    cFile.write ('    // No else: skipped no error \n')
    cFile.write ('    \n')
    
    cFile.write ('    // return the error\n')
    cFile.write ('    if (error != NULL)\n')
    cFile.write ('    {\n')
    cFile.write ('        *error = localError;\n')
    cFile.write ('    }\n')
    cFile.write ('    // No else: error is not returned \n')
    cFile.write ('    \n')
    
    cFile.write ('    return deviceController;\n')
    cFile.write ('}\n')
    cFile.write ('\n')
    
    cFile.write ('void ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'Delete')+' ('+className+' **deviceController)\n')
    cFile.write ('{\n')
    
    cFile.write ('    ARSAL_PRINT(ARSAL_PRINT_INFO, '+MODULE_DEVICE+'_TAG, "Delete ...");\n')
    
    cFile.write ('    // -- Delete the Device Controller --\n')
    cFile.write ('    \n')

    cFile.write ('    if (deviceController != NULL)\n')
    cFile.write ('    {\n')
    cFile.write ('        if ((*deviceController) != NULL)\n')
    cFile.write ('        {\n')
    
    cFile.write ('            '+ ARFunctionName (MODULE_ARCONTROLLER, 'device', 'Stop')+' (*deviceController);\n')
    
    cFile.write ('            if ((*deviceController)->privatePart != NULL)\n')
    cFile.write ('            {\n')
    cFile.write ('                ARSAL_Mutex_Destroy (&((*deviceController)->privatePart->mutex));\n')
    cFile.write ('                \n')
    
    cFile.write ('                // Delete features:\n')
    cFile.write ('                switch ((*deviceController)->privatePart->discoveryDevice->productID)\n')
    cFile.write ('                {\n')
    for deviceController in deviceControllers:
        cFile.write ('                    case '+discoveryProduct (deviceController.product)+':\n')
        for featureName in deviceController.features:
            cFile.write ('    ARSAL_PRINT(ARSAL_PRINT_INFO, '+MODULE_DEVICE+'_TAG, "' + ARFunctionName (MODULE_FEATURE, featureName, 'Delete')+' ...");\n')
            cFile.write ('                        ' + ARFunctionName (MODULE_FEATURE, featureName, 'Delete')+' (&((*deviceController)->'+ARUncapitalize(featureName)+'));\n')
            cFile.write ('                        \n')
        cFile.write ('                        break;\n')
        cFile.write ('                    \n')
    
    cFile.write ('                    default:\n')
    cFile.write ('                        ARSAL_PRINT(ARSAL_PRINT_ERROR, '+MODULE_DEVICE+'_TAG, "device : %d not known", (*deviceController)->privatePart->discoveryDevice->productID);\n')
    cFile.write ('                        break;\n')
    cFile.write ('                }\n')
    cFile.write ('                \n')
    
    cFile.write ('                ARDISCOVERY_Device_Delete (&((*deviceController)->privatePart->discoveryDevice));\n')
    cFile.write ('                \n')
    
    cFile.write ('                // Stop network:\n')
    cFile.write ('                ARCONTROLLER_Network_Stop ((*deviceController)->privatePart->networkController); //TODO read error !!!!!!!! \n')
    cFile.write ('                \n')
    
    cFile.write ('                // Delete network:\n')
    cFile.write ('                ' + ARFunctionName (MODULE_ARCONTROLLER, "Network", 'Delete') + ' (&((*deviceController)->privatePart->networkController)); //TODO read error !!!!!!!! \n')
    cFile.write ('                \n')
    
    cFile.write ('                // free the private part of the Device Controller\n')
    cFile.write ('                free ((*deviceController)->privatePart);\n')
    cFile.write ('                (*deviceController)->privatePart = NULL;\n')
    cFile.write ('            }\n')
    cFile.write ('            \n')
    
    cFile.write ('            // free the Device Controller\n')
    cFile.write ('            free (*deviceController);\n')
    cFile.write ('            (*deviceController) = NULL;\n')
    cFile.write ('        }\n')
    cFile.write ('    }\n')
    cFile.write ('}\n')
    cFile.write ('\n')
    
    cFile.write ('eARCONTROLLER_ERROR ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'RegisterCallbacks')+' ('+className+' *deviceController)\n')
    cFile.write ('{\n')
    
    cFile.write ('    ARSAL_PRINT(ARSAL_PRINT_INFO, '+MODULE_DEVICE+'_TAG, "Register the Callbacks ...");\n')
    
    cFile.write ('    // Register the Callbacks \n')
    cFile.write ('    \n')
    cFile.write ('    eARCONTROLLER_ERROR error = ARCONTROLLER_OK;\n')
    cFile.write ('    \n')
    
    cFile.write ('    // check parameters\n')
    cFile.write ('    if (deviceController == NULL)\n')
    cFile.write ('    {\n')
    cFile.write ('        error = ARCONTROLLER_ERROR_BAD_PARAMETER;\n')
    cFile.write ('    }\n')
    cFile.write ('    // No Else: the checking parameters sets localError to ARNETWORK_ERROR_BAD_PARAMETER and stop the processing\n')
    cFile.write ('    \n')
    
    for feature in allFeatures:
        cFile.write ('    if (deviceController->'+ARUncapitalize(feature.name)+' != NULL)\n')
        cFile.write ('    {\n')
        for cl in feature.classes:
            
            if isState(cl):
                for cmd in cl.cmds:
                    cFile.write ('        if (error == ARCONTROLLER_OK)\n')
                    cFile.write ('        {\n')
                    cFile.write ('            error = '+ARFunctionName(MODULE_FEATURE, feature.name, 'addCallback')+' (deviceController->'+ARUncapitalize(feature.name)+', '+defineNotification(MODULE_FEATURE, feature, cl, cmd)+', ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'DictionaryChangedCallback')+', deviceController);\n')
                    cFile.write ('        }\n')
                    cFile.write ('        \n')
        cFile.write ('    }\n')
        cFile.write ('    \n')
        
    cFile.write ('    ARSAL_PRINT(ARSAL_PRINT_INFO, '+MODULE_DEVICE+'_TAG, "Register the Callbacks ... error:%d", error);\n')
        
    cFile.write ('    return error;\n')
    cFile.write ('}\n')
    cFile.write ('\n')
    
    cFile.write ('eARCONTROLLER_ERROR ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'UnregisterCallbacks')+' ('+className+' *deviceController)\n')
    cFile.write ('{\n')
    cFile.write ('    // Unregister the Callbacks \n')
    cFile.write ('    \n')
    cFile.write ('    eARCONTROLLER_ERROR error = ARCONTROLLER_OK;\n')
    cFile.write ('    eARCONTROLLER_ERROR removingError = ARCONTROLLER_OK;\n')
    cFile.write ('    \n')
    
    cFile.write ('    // check parameters\n')
    cFile.write ('    if (deviceController == NULL)\n')
    cFile.write ('    {\n')
    cFile.write ('        error = ARCONTROLLER_ERROR_BAD_PARAMETER;\n')
    cFile.write ('    }\n')
    cFile.write ('    // No Else: the checking parameters sets localError to ARNETWORK_ERROR_BAD_PARAMETER and stop the processing\n')
    cFile.write ('    \n')
    
    cFile.write ('    if (error == ARCONTROLLER_OK)\n')
    cFile.write ('    {\n')
    
    for feature in allFeatures:
        cFile.write ('        if (deviceController->'+ARUncapitalize(feature.name)+' != NULL)\n')
        cFile.write ('        {\n')
        for cl in feature.classes:
            if isState(cl):
                for cmd in cl.cmds:
                    cFile.write ('            removingError = '+ARFunctionName(MODULE_FEATURE, feature.name, 'removeCallback')+' (deviceController->'+ARUncapitalize(feature.name)+', '+defineNotification(MODULE_FEATURE, feature, cl, cmd)+', ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'DictionaryChangedCallback')+', deviceController);\n')
                    cFile.write ('            if (error == ARCONTROLLER_OK)\n')
                    cFile.write ('            {\n')
                    cFile.write ('                ARSAL_PRINT(ARSAL_PRINT_ERROR, '+MODULE_DEVICE+'_TAG, "Error occured durring removing of the callback for '+defineNotification(MODULE_FEATURE, feature, cl, cmd)+'; error :%s", ARCONTROLLER_Error_ToString (removingError));\n')
                    cFile.write ('            }\n')
                    cFile.write ('            \n')
            
        cFile.write ('        }\n')
        cFile.write ('        \n')
            
    cFile.write ('    }\n')
    cFile.write ('    \n')
            
    cFile.write ('    return error;\n')
    cFile.write ('}\n')
    cFile.write ('\n')
    
    cFile.write ('eARCONTROLLER_ERROR ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'Start')+' ('+className+' *deviceController)\n')
    cFile.write ('{\n')
    cFile.write ('    // Start the Device Controller \n')
    cFile.write ('    \n')
    cFile.write ('    eARCONTROLLER_ERROR error = ARCONTROLLER_OK;\n')
    cFile.write ('    \n')
    
    cFile.write ('    // check parameters\n')
    cFile.write ('    if (deviceController == NULL)\n')
    cFile.write ('    {\n')
    cFile.write ('        error = ARCONTROLLER_ERROR_BAD_PARAMETER;\n')
    cFile.write ('    }\n')
    cFile.write ('    // No Else: the checking parameters sets localError to ARNETWORK_ERROR_BAD_PARAMETER and stop the processing\n')
    cFile.write ('    \n')
    
    cFile.write ('    if (error == ARCONTROLLER_OK)\n')
    cFile.write ('    {\n')
    cFile.write ('        error = ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'RegisterCallbacks')+' (deviceController);\n')
    cFile.write ('    }\n')
    cFile.write ('    \n')
            
    cFile.write ('    return error;\n')
    cFile.write ('}\n')
    cFile.write ('\n')
    
    cFile.write ('eARCONTROLLER_ERROR ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'Stop')+' ('+className+' *deviceController)\n')
    cFile.write ('{\n')
    cFile.write ('    // Stop the Device Controller \n')
    cFile.write ('    \n')
    cFile.write ('    eARCONTROLLER_ERROR error = ARCONTROLLER_OK;\n')
    cFile.write ('    \n')
    
    cFile.write ('    // check parameters\n')
    cFile.write ('    if (deviceController == NULL)\n')
    cFile.write ('    {\n')
    cFile.write ('        error = ARCONTROLLER_ERROR_BAD_PARAMETER;\n')
    cFile.write ('    }\n')
    cFile.write ('    // No Else: the checking parameters sets localError to ARNETWORK_ERROR_BAD_PARAMETER and stop the processing\n')
    cFile.write ('    \n')
    
    cFile.write ('    if (error == ARCONTROLLER_OK)\n')
    cFile.write ('    {\n')
    cFile.write ('        error = ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'UnregisterCallbacks')+' (deviceController);\n')
    cFile.write ('    }\n')
    cFile.write ('    \n')
            
    cFile.write ('    return error;\n')
    cFile.write ('}\n')
    cFile.write ('\n')
    
    cFile.write ('//eARCONTROLLER_ERROR ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'SetInitialDate')+' ('+className+' *deviceController)\n')
    
    cFile.write ('//eARCONTROLLER_ERROR ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'GetInitialSettings')+' ('+className+' *deviceController)\n')
    
    cFile.write ('eARCONTROLLER_ERROR ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'getInitialStates')+' ('+className+' *deviceController)\n')
    cFile.write ('{\n')
    cFile.write ('    // Get all states \n')
    cFile.write ('    \n')
    cFile.write ('    eARCONTROLLER_ERROR error = ARCONTROLLER_OK;\n')
    cFile.write ('    \n')
    
    cFile.write ('    // check parameters\n')
    cFile.write ('    if (deviceController == NULL)\n')
    cFile.write ('    {\n')
    cFile.write ('        error = ARCONTROLLER_ERROR_BAD_PARAMETER;\n')
    cFile.write ('    }\n')
    cFile.write ('    // No Else: the checking parameters sets localError to ARNETWORK_ERROR_BAD_PARAMETER and stop the processing\n')
    cFile.write ('    \n')
    
    cFile.write ('    if (error == ARCONTROLLER_OK)\n')
    cFile.write ('    {\n')
    cFile.write ('        error = deviceController->common->sendCommonAllStates (deviceController->common);\n')
    cFile.write ('    }\n')
    cFile.write ('    \n')
            
    cFile.write ('    return error;\n')
    cFile.write ('}\n')
    cFile.write ('\n')
    
    
    cFile.write ('void ' + ARFunctionName (MODULE_ARCONTROLLER, 'device', 'DictionaryChangedCallback')+' (int commandKey, ARCONTROLLER_FEATURE_DICTIONARY_ARG_t *argumentDictionary, void *customData)\n')
    cFile.write ('{\n')
    cFile.write ('    ARSAL_PRINT(ARSAL_PRINT_ERROR, '+MODULE_DEVICE+'_TAG, "DictionaryChangedCallback ... ");\n')
    cFile.write ('    ARSAL_PRINT(ARSAL_PRINT_ERROR, '+MODULE_DEVICE+'_TAG, "commandKey : %d ", commandKey);\n')
    cFile.write ('    ARSAL_PRINT(ARSAL_PRINT_ERROR, '+MODULE_DEVICE+'_TAG, "argumentDictionary : %p ", argumentDictionary);\n')
    cFile.write ('    ARSAL_PRINT(ARSAL_PRINT_ERROR, '+MODULE_DEVICE+'_TAG, "customData : %p ", customData);\n')
    cFile.write ('}\n')
    cFile.write ('\n')
    
    cFile.close ()

