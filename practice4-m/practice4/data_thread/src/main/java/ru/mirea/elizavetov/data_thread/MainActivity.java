package ru.mirea.elizavetov.data_thread;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

import java.util.concurrent.TimeUnit;

public class MainActivity extends AppCompatActivity {
    TextView tvInfo;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        tvInfo = findViewById(R.id.TextView);
        final Runnable runn1 = new Runnable() {
            public void run() {
                tvInfo.setText("runn1");
            }
        };
        final Runnable runn2 = new Runnable() {
            public void run() {
                tvInfo.setText("runn2");
            }
        };
        final Runnable runn3 = new Runnable() {
            public void run() {
                tvInfo.setText("runn3");
            }
        };
        Thread t = new Thread(new Runnable() {
            public void run() {
                try {
                    TimeUnit.SECONDS.sleep(2);
                    /*Запускает задачу по изменению пользовательского интерфейс, которая
                     *выполняются сразу же, если является текущим потоком, иначе добавляется в очередь событий*/
                    runOnUiThread(runn1);
                    TimeUnit.SECONDS.sleep(1);
                    /*Поток будет запущен по истечении указанного количества времени*/
                    tvInfo.postDelayed(runn3, 2000);
                    /*Добавляет задачу в очередь для запуска*/
                    tvInfo.post(runn2);

                    //сначала выполнится runn1, через секунду после выполнится runn2, через 2 секунды после выполнится runn3
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });
        t.start();
    }
}