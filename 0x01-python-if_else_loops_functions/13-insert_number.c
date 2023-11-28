#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a node into a sorted singly linked list.
 * @head: Pointer to a pointer to the head of the list.
 * @number: Integer value to insert into the list.
 *
 * Return: Pointer to the newly inserted node, or NULL on failure.
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node, *current_node;


new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
return (NULL);

if (*head == NULL || number <= (*head)->n)
{
new_node->n = number;
new_node->next = *head;
*head = new_node;
return (new_node);
}
else
{
current_node = *head;
while (current_node->next != NULL && number > current_node->next->n)
{
current_node = current_node->next;
}

new_node->n = number;
new_node->next = current_node->next;
current_node->next = new_node;
return (new_node);
}
}
