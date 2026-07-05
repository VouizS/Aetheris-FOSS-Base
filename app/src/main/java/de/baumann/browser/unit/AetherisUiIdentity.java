package de.baumann.browser.unit;

import android.app.Activity;
import android.graphics.Color;
import android.os.Build;
import android.view.View;
import android.view.Window;

public final class AetherisUiIdentity {

    private AetherisUiIdentity() {
    }

    public static void apply(Activity activity) {
        if (activity == null) {
            return;
        }

        try {
            Window window = activity.getWindow();

            if (window != null) {
                window.setStatusBarColor(Color.parseColor("#050914"));
                window.setNavigationBarColor(Color.parseColor("#07101F"));

                if (Build.VERSION.SDK_INT >= 23) {
                    View decor = window.getDecorView();
                    if (decor != null) {
                        decor.setSystemUiVisibility(0);
                    }
                }
            }
        } catch (Exception ignored) {
        }
    }
}
