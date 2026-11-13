package com.stusta.arabiclearning;

import android.content.ComponentName;
import android.content.pm.PackageManager;
import com.getcapacitor.JSObject;
import com.getcapacitor.Plugin;
import com.getcapacitor.PluginCall;
import com.getcapacitor.PluginMethod;
import com.getcapacitor.annotation.CapacitorPlugin;
import java.util.Map;
import java.util.LinkedHashMap;

@CapacitorPlugin(name = "AppIcon")
public class AppIconPlugin extends Plugin {
    private static final Map<String, String> ALIASES = new LinkedHashMap<>();
    static {
        ALIASES.put("green", "IconGreen"); ALIASES.put("blue", "IconBlue");
        ALIASES.put("rose", "IconRose"); ALIASES.put("amber", "IconAmber");
        ALIASES.put("purple", "IconPurple");
    }

    @PluginMethod
    public void setColor(PluginCall call) {
        String color = call.getString("color", "green");
        String selected = ALIASES.get(color);
        if (selected == null) { call.reject("Unsupported icon color"); return; }
        PackageManager manager = getContext().getPackageManager();
        String packageName = getContext().getPackageName();
        try {
            // Enable the new entry before disabling any others so there is always a launcher.
            manager.setComponentEnabledSetting(new ComponentName(packageName, packageName + "." + selected),
                PackageManager.COMPONENT_ENABLED_STATE_ENABLED, PackageManager.DONT_KILL_APP);
            for (String alias : ALIASES.values()) {
                if (!alias.equals(selected)) manager.setComponentEnabledSetting(
                    new ComponentName(packageName, packageName + "." + alias),
                    PackageManager.COMPONENT_ENABLED_STATE_DISABLED, PackageManager.DONT_KILL_APP);
            }
            JSObject result = new JSObject(); result.put("color", color); call.resolve(result);
        } catch (Exception error) { call.reject("Unable to update launcher icon", error); }
    }
}
