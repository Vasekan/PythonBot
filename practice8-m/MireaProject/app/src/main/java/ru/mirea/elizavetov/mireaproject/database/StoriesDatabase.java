package ru.mirea.elizavetov.mireaproject.database;

import androidx.room.Database;
import androidx.room.RoomDatabase;

import ru.mirea.elizavetov.mireaproject.ui.story.Story;
import ru.mirea.elizavetov.mireaproject.ui.story.StoryDao;

@Database(entities = {Story.class}, version = 1)
public abstract class StoriesDatabase extends RoomDatabase {

    public abstract StoryDao storyDAO();
}
