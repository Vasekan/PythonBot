package ru.mirea.elizavetov.intentapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;

public class Second extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);

        Intent intent = getIntent();
        String string = intent.getStringExtra("time");

        TextView textView = (TextView) findViewById(R.id.textView);
        textView.setText(string);
    }
}