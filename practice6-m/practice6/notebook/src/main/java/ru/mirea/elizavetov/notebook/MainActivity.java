package ru.mirea.elizavetov.notebook;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.Environment;
import android.view.View;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;

public class MainActivity extends AppCompatActivity {
    private SharedPreferences preferences;
    final String SAVED_TEXT = "saved_text";
    private static final String LOG_TAG = MainActivity.class.getSimpleName();

    private String name, text;
    private File file;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        EditText nameOfTheFile = findViewById(R.id.nameOfTheFile);
        EditText textOfTheFile = findViewById(R.id.textOfTheFile);

        name = nameOfTheFile.getText().toString();
        text = textOfTheFile.getText().toString();

    }

    public void onSave(View view){
        if (isExternalStorageWritable()){
            file = new File(getExternalFilesDir(null), name);
            FileOutputStream outputStream = null;
            try {
                file.createNewFile();
                outputStream = new FileOutputStream(file, true);

                outputStream.write(text.getBytes());
                outputStream.flush();
                outputStream.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }


    /* Проверяем хранилище на доступность чтения и записи*/
    public boolean isExternalStorageWritable() {
        String state = Environment.getExternalStorageState();
        return Environment.MEDIA_MOUNTED.equals(state);
    }

    public void onLoad(View view){
        StringBuilder text = new StringBuilder();

        try {
            BufferedReader br = new BufferedReader(new FileReader(file));
            String line;

            while ((line = br.readLine()) != null){
                text.append(line);
                text.append("\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}