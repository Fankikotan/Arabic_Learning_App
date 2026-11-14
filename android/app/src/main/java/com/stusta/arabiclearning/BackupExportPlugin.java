package com.stusta.arabiclearning;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import androidx.activity.result.ActivityResult;
import com.getcapacitor.JSObject;
import com.getcapacitor.Plugin;
import com.getcapacitor.PluginCall;
import com.getcapacitor.PluginMethod;
import com.getcapacitor.annotation.ActivityCallback;
import com.getcapacitor.annotation.CapacitorPlugin;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.atomic.AtomicBoolean;
import org.json.JSONObject;

@CapacitorPlugin(name = "BackupExport")
public class BackupExportPlugin extends Plugin {
    private final AtomicBoolean saving = new AtomicBoolean(false);

    @PluginMethod
    public void saveBackup(PluginCall call) {
        String json = call.getString("json");
        try {
            if (json == null || !"arabic-learning-backup".equals(new JSONObject(json).optString("format"))) {
                call.reject("Invalid learning backup"); return;
            }
        } catch (Exception error) { call.reject("Invalid backup JSON", error); return; }
        if (!saving.compareAndSet(false, true)) { call.reject("A backup save is already open"); return; }
        String filename = call.getString("filename", "arabic-learning-backup.json");
        filename = filename.replaceAll("[\\\\/\\r\\n]", "_");
        if (!filename.endsWith(".json")) filename += ".json";
        Intent intent = new Intent(Intent.ACTION_CREATE_DOCUMENT);
        intent.addCategory(Intent.CATEGORY_OPENABLE);
        intent.setType("application/json");
        intent.putExtra(Intent.EXTRA_TITLE, filename);
        try { startActivityForResult(call, intent, "onBackupLocation"); }
        catch (Exception error) { saving.set(false); call.reject("Unable to open system save dialog", error); }
    }

    @ActivityCallback
    private void onBackupLocation(PluginCall call, ActivityResult result) {
        if (call == null) { saving.set(false); return; }
        if (result.getResultCode() != Activity.RESULT_OK) {
            saving.set(false); JSObject value = new JSObject(); value.put("cancelled", true); call.resolve(value); return;
        }
        Uri uri = result.getData() == null ? null : result.getData().getData();
        if (uri == null) { saving.set(false); call.reject("No save location returned"); return; }
        execute(() -> {
            try {
                byte[] bytes = call.getString("json", "").getBytes(StandardCharsets.UTF_8);
                try (OutputStream stream = getContext().getContentResolver().openOutputStream(uri, "wt")) {
                    if (stream == null) throw new java.io.IOException("Cannot open selected location");
                    stream.write(bytes); stream.flush();
                }
                JSObject value = new JSObject(); value.put("saved", true); value.put("bytes", bytes.length); call.resolve(value);
            } catch (Exception error) { call.reject("Unable to save backup: " + error.getMessage(), error); }
            finally { saving.set(false); }
        });
    }
}
